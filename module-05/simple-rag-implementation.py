"""
Simple RAG Implementation using ChromaDB and OpenAI
====================================================

This script demonstrates a complete, self-contained RAG (Retrieval-Augmented
Generation) pipeline using ChromaDB as the vector database and OpenAI for
embeddings and text generation.

Requirements:
    pip install openai chromadb python-dotenv tiktoken PyPDF2

Usage:
    1. Set your OPENAI_API_KEY environment variable or create a .env file
    2. Place documents in a ./documents/ directory
    3. Run: python simple-rag-implementation.py

Author: Master in Prompt Engineering and AI - Module 05
"""

import os
import re
import json
from typing import List, Dict, Optional
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from chromadb.utils import embedding_functions

# Load environment variables
load_dotenv()


# =============================================================================
# CONFIGURATION
# =============================================================================

class RAGConfig:
    """Configuration for the RAG system."""
    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-4o"
    LLM_TEMPERATURE = 0.1
    LLM_MAX_TOKENS = 1000

    # Chunking
    CHUNK_SIZE = 800          # Characters per chunk
    CHUNK_OVERLAP = 100       # Overlap between chunks

    # Retrieval
    TOP_K = 5                 # Number of chunks to retrieve
    MIN_RELEVANCE = 0.3       # Minimum relevance score (0-1)

    # Storage
    CHROMA_DB_PATH = "./rag_chroma_db"
    COLLECTION_NAME = "documents"
    DOCUMENTS_DIR = "./documents"


# =============================================================================
# DOCUMENT LOADING
# =============================================================================

def load_text_file(file_path: str) -> str:
    """Load content from a plain text or markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf_file(file_path: str) -> str:
    """Load content from a PDF file."""
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        pages = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                pages.append(f"[Page {i + 1}]\n{text}")
        return "\n\n".join(pages)
    except ImportError:
        print("Warning: PyPDF2 not installed. Skipping PDF files.")
        return ""


def load_document(file_path: str) -> Dict:
    """
    Load a document and return its content with metadata.

    Returns:
        Dict with 'content' and 'metadata' keys.
    """
    filename = os.path.basename(file_path)
    ext = os.path.splitext(filename)[1].lower()

    if ext in (".txt", ".md"):
        content = load_text_file(file_path)
    elif ext == ".pdf":
        content = load_pdf_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return {
        "content": content,
        "metadata": {
            "source": filename,
            "file_path": file_path,
            "file_type": ext,
            "char_count": len(content),
        }
    }


def load_all_documents(directory: str = None) -> List[Dict]:
    """Load all supported documents from a directory."""
    directory = directory or RAGConfig.DOCUMENTS_DIR
    documents = []
    supported = {".txt", ".md", ".pdf"}

    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        print("Creating directory. Please add documents and run again.")
        os.makedirs(directory, exist_ok=True)
        return documents

    for filename in sorted(os.listdir(directory)):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in supported:
            continue

        file_path = os.path.join(directory, filename)
        try:
            doc = load_document(file_path)
            documents.append(doc)
            print(f"  Loaded: {filename} ({doc['metadata']['char_count']} chars)")
        except Exception as e:
            print(f"  Error loading {filename}: {e}")

    return documents


# =============================================================================
# CHUNKING
# =============================================================================

def chunk_text(
    text: str,
    chunk_size: int = None,
    overlap: int = None
) -> List[str]:
    """
    Split text into overlapping chunks, trying to break at natural boundaries.

    Uses a recursive splitting strategy:
    1. Try to split at paragraph boundaries (\\n\\n)
    2. Fall back to sentence boundaries (. )
    3. Fall back to word boundaries ( )
    4. Last resort: split at character boundaries

    Args:
        text: The text to chunk
        chunk_size: Maximum characters per chunk
        overlap: Number of overlapping characters

    Returns:
        List of text chunks
    """
    chunk_size = chunk_size or RAGConfig.CHUNK_SIZE
    overlap = overlap or RAGConfig.CHUNK_OVERLAP

    # Clean the text
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        if end >= len(text):
            # Last chunk - take everything remaining
            chunk = text[start:].strip()
            if chunk:
                chunks.append(chunk)
            break

        # Try to find a good break point
        chunk_text_segment = text[start:end]

        # Try paragraph break
        break_point = chunk_text_segment.rfind("\n\n")
        if break_point == -1 or break_point < chunk_size * 0.3:
            # Try sentence break
            break_point = chunk_text_segment.rfind(". ")
            if break_point != -1:
                break_point += 2  # Include the period and space

        if break_point == -1 or break_point < chunk_size * 0.3:
            # Try any newline
            break_point = chunk_text_segment.rfind("\n")

        if break_point == -1 or break_point < chunk_size * 0.3:
            # Try word break
            break_point = chunk_text_segment.rfind(" ")

        if break_point == -1 or break_point < chunk_size * 0.3:
            # Hard split
            break_point = chunk_size

        actual_end = start + break_point
        chunk = text[start:actual_end].strip()

        if chunk:
            chunks.append(chunk)

        # Move start position, accounting for overlap
        start = actual_end - overlap
        if start <= (actual_end - chunk_size):
            start = actual_end  # Prevent infinite loop

    return chunks


def chunk_documents(documents: List[Dict]) -> List[Dict]:
    """
    Chunk all documents and return chunks with metadata.

    Returns:
        List of dicts with 'text' and 'metadata' keys
    """
    all_chunks = []

    for doc in documents:
        text_chunks = chunk_text(doc["content"])

        for i, chunk in enumerate(text_chunks):
            all_chunks.append({
                "text": chunk,
                "metadata": {
                    **doc["metadata"],
                    "chunk_index": i,
                    "total_chunks": len(text_chunks),
                }
            })

    return all_chunks


# =============================================================================
# VECTOR STORE
# =============================================================================

class SimpleVectorStore:
    """Simple vector store wrapper around ChromaDB."""

    def __init__(self):
        self.client = chromadb.PersistentClient(path=RAGConfig.CHROMA_DB_PATH)
        self.embedding_fn = embedding_functions.OpenAIEmbeddingFunction(
            api_key=RAGConfig.OPENAI_API_KEY,
            model_name=RAGConfig.EMBEDDING_MODEL,
        )
        self.collection = self.client.get_or_create_collection(
            name=RAGConfig.COLLECTION_NAME,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )

    def add_chunks(self, chunks: List[Dict]) -> int:
        """Add chunks to the vector store. Returns count of chunks added."""
        if not chunks:
            return 0

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):
            chunk_id = f"{chunk['metadata']['source']}_chunk_{i}"
            ids.append(chunk_id)
            documents.append(chunk["text"])

            # Flatten metadata for ChromaDB (must be str, int, float, or bool)
            flat_meta = {}
            for k, v in chunk["metadata"].items():
                if isinstance(v, (str, int, float, bool)):
                    flat_meta[k] = v
                else:
                    flat_meta[k] = str(v)
            metadatas.append(flat_meta)

        # Add in batches
        batch_size = 500
        for start in range(0, len(ids), batch_size):
            end = start + batch_size
            self.collection.add(
                ids=ids[start:end],
                documents=documents[start:end],
                metadatas=metadatas[start:end],
            )

        return len(ids)

    def search(self, query: str, top_k: int = None) -> List[Dict]:
        """
        Search for relevant chunks.

        Returns:
            List of dicts with 'text', 'metadata', 'score' keys.
        """
        top_k = top_k or RAGConfig.TOP_K

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
        )

        search_results = []
        for i in range(len(results["documents"][0])):
            distance = results["distances"][0][i]
            score = 1 - distance  # Convert distance to similarity

            if score < RAGConfig.MIN_RELEVANCE:
                continue

            search_results.append({
                "text": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "score": round(score, 4),
            })

        return search_results

    @property
    def count(self) -> int:
        """Number of chunks in the store."""
        return self.collection.count()

    def clear(self):
        """Remove all documents from the collection."""
        self.client.delete_collection(RAGConfig.COLLECTION_NAME)
        self.collection = self.client.get_or_create_collection(
            name=RAGConfig.COLLECTION_NAME,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )


# =============================================================================
# RAG PIPELINE
# =============================================================================

class RAGPipeline:
    """Complete RAG pipeline: ingest, retrieve, and generate."""

    def __init__(self):
        self.openai = OpenAI(api_key=RAGConfig.OPENAI_API_KEY)
        self.vector_store = SimpleVectorStore()

    # ─── Ingestion ───────────────────────────────────────────────

    def ingest(self, directory: str = None):
        """Load, chunk, and index documents from a directory."""
        print("\n=== Document Ingestion ===")

        # Load documents
        print("Loading documents...")
        documents = load_all_documents(directory)
        if not documents:
            print("No documents found.")
            return

        # Chunk documents
        print(f"\nChunking {len(documents)} documents...")
        chunks = chunk_documents(documents)
        print(f"Created {len(chunks)} chunks")

        # Index chunks
        print("Indexing chunks into vector store...")
        count = self.vector_store.add_chunks(chunks)
        print(f"Indexed {count} chunks successfully")
        print(f"Total chunks in store: {self.vector_store.count}")

    # ─── Retrieval ───────────────────────────────────────────────

    def retrieve(self, query: str, top_k: int = None) -> List[Dict]:
        """Retrieve relevant chunks for a query."""
        return self.vector_store.search(query, top_k)

    # ─── Generation ──────────────────────────────────────────────

    def generate(self, query: str, context_chunks: List[Dict]) -> str:
        """Generate an answer using the LLM with retrieved context."""

        # Format context
        if context_chunks:
            context_parts = []
            for i, chunk in enumerate(context_chunks, 1):
                source = chunk["metadata"].get("source", "Unknown")
                score = chunk["score"]
                context_parts.append(
                    f"[Source: {source} | Relevance: {score}]\n{chunk['text']}"
                )
            context = "\n\n---\n\n".join(context_parts)
        else:
            context = "No relevant documents were found."

        # Build the prompt
        prompt = f"""Use the following context to answer the user's question.
If the context does not contain enough information to answer fully,
say so clearly. Always cite the source document(s) you reference.

CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:"""

        # Call the LLM
        response = self.openai.chat.completions.create(
            model=RAGConfig.LLM_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that answers questions "
                        "based on provided document context. Be accurate, "
                        "cite your sources, and clearly indicate when you "
                        "are unsure or the context is insufficient."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=RAGConfig.LLM_TEMPERATURE,
            max_tokens=RAGConfig.LLM_MAX_TOKENS,
        )

        return response.choices[0].message.content

    # ─── Complete Query Pipeline ─────────────────────────────────

    def query(self, question: str, top_k: int = None) -> Dict:
        """
        Run the complete RAG pipeline: retrieve context and generate answer.

        Args:
            question: The user's question
            top_k: Number of chunks to retrieve

        Returns:
            Dict with 'answer', 'sources', 'num_chunks_retrieved'
        """
        # Step 1: Retrieve
        chunks = self.retrieve(question, top_k)

        # Step 2: Generate
        answer = self.generate(question, chunks)

        # Step 3: Compile sources
        sources = [
            {
                "source": c["metadata"].get("source", "Unknown"),
                "relevance": c["score"],
                "preview": c["text"][:120] + "...",
            }
            for c in chunks
        ]

        return {
            "answer": answer,
            "sources": sources,
            "num_chunks_retrieved": len(chunks),
        }


# =============================================================================
# MAIN - INTERACTIVE DEMO
# =============================================================================

def print_divider():
    print("-" * 60)


def print_result(result: Dict):
    """Pretty-print a query result."""
    print_divider()
    print("ANSWER:")
    print_divider()
    print(result["answer"])

    if result["sources"]:
        print()
        print_divider()
        print(f"SOURCES ({result['num_chunks_retrieved']} chunks retrieved):")
        print_divider()
        for src in result["sources"]:
            print(f"  [{src['relevance']}] {src['source']}")
            print(f"        {src['preview']}")
    print()


def main():
    """Interactive RAG demo."""
    print("=" * 60)
    print("  SIMPLE RAG IMPLEMENTATION")
    print("  Using ChromaDB + OpenAI")
    print("=" * 60)

    # Verify API key
    if not RAGConfig.OPENAI_API_KEY:
        print("\nError: OPENAI_API_KEY not set.")
        print("Set it in your environment or create a .env file.")
        return

    # Initialize pipeline
    rag = RAGPipeline()

    # Check if documents need to be ingested
    if rag.vector_store.count == 0:
        print(f"\nNo documents indexed. Looking in {RAGConfig.DOCUMENTS_DIR}/...")
        rag.ingest()

        if rag.vector_store.count == 0:
            print(f"\nNo documents found. Add .txt, .md, or .pdf files to "
                  f"{RAGConfig.DOCUMENTS_DIR}/ and run again.")
            return

    print(f"\nKnowledge base: {rag.vector_store.count} chunks indexed")
    print("\nType your questions below. Commands:")
    print("  /ingest  - Re-ingest documents")
    print("  /clear   - Clear the vector store")
    print("  /quit    - Exit")
    print()

    while True:
        try:
            user_input = input("Question: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("/quit", "/exit", "/q"):
            print("Goodbye!")
            break
        if user_input.lower() == "/ingest":
            rag.vector_store.clear()
            rag.ingest()
            continue
        if user_input.lower() == "/clear":
            rag.vector_store.clear()
            print("Vector store cleared.")
            continue

        # Query the RAG pipeline
        print("Searching and generating...")
        result = rag.query(user_input)
        print_result(result)


if __name__ == "__main__":
    main()
