# Chunking Strategies Guide

## Module 05: Code and Examples

---

## Why Chunking Matters

Chunking is the process of splitting documents into smaller pieces for embedding and retrieval. It is arguably the **single most impactful decision** in a RAG pipeline. Poor chunking leads to poor retrieval, which leads to poor answers -- no amount of prompt engineering can fix bad chunks.

---

## The Core Trade-offs

```
SMALLER CHUNKS                         LARGER CHUNKS
  + More precise retrieval               + More context per chunk
  + Better semantic focus                 + Fewer chunks to manage
  + Less noise in results                 + Preserves longer arguments
  - May lose context                      - May include irrelevant content
  - May split related info                - Less precise retrieval
  - More chunks to process                - Harder to fit in context window

SWEET SPOT: 200-1000 tokens (depending on use case)
```

---

## Strategy 1: Fixed-Size Chunking

The simplest approach: split text into chunks of N characters or tokens.

### How It Works

```
Document: "AAAAABBBBBCCCCCDDDDDEEEEE" (25 chars)

Chunk size: 10, No overlap:
  Chunk 1: "AAAAABBBBB"
  Chunk 2: "CCCCCDDDDD"
  Chunk 3: "EEEEE"

Chunk size: 10, Overlap: 3:
  Chunk 1: "AAAAABBBBB"
  Chunk 2: "BBBCCCCCDD"
  Chunk 3: "DDDEEEEE"
```

### Implementation

```python
def fixed_size_chunk(text, chunk_size=500, overlap=50):
    """Split text into fixed-size chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
```

### When to Use
- Quick prototyping
- Uniform-length documents
- When simplicity matters more than quality

### When NOT to Use
- Documents with meaningful structure
- When semantic coherence is important
- Technical or legal documents

---

## Strategy 2: Sentence-Based Chunking

Split at sentence boundaries, grouping sentences to reach a target chunk size.

### How It Works

```
Input paragraph:
  "AI is transforming industries. Machine learning is a subset of AI.
   Deep learning uses neural networks. RAG combines retrieval with generation.
   Fine-tuning adapts models to specific tasks."

Target: ~2 sentences per chunk

  Chunk 1: "AI is transforming industries. Machine learning is a subset of AI."
  Chunk 2: "Deep learning uses neural networks. RAG combines retrieval with generation."
  Chunk 3: "Fine-tuning adapts models to specific tasks."
```

### Implementation

```python
import re

def sentence_chunk(text, max_sentences=5, max_chars=1000):
    """Split text into chunks of N sentences, respecting a max character limit."""
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current = []
    current_len = 0

    for sentence in sentences:
        if (len(current) >= max_sentences or
            current_len + len(sentence) > max_chars) and current:
            chunks.append(" ".join(current))
            current = []
            current_len = 0

        current.append(sentence)
        current_len += len(sentence)

    if current:
        chunks.append(" ".join(current))

    return chunks
```

### When to Use
- General prose documents
- FAQ sections
- News articles and blog posts

### When NOT to Use
- Code (sentences don't apply to code)
- Highly structured documents (tables, forms)

---

## Strategy 3: Recursive Character Text Splitting

LangChain's default strategy. Tries to split by the most meaningful separator first, then falls back to smaller separators.

### How It Works

```
Separator hierarchy:
  1. "\n\n" (paragraph boundaries)   -- Most meaningful
  2. "\n"   (line boundaries)
  3. ". "   (sentence boundaries)
  4. " "    (word boundaries)
  5. ""     (character boundaries)    -- Least meaningful

The algorithm:
  1. Try splitting by "\n\n"
  2. For each piece, if it's still too large, try splitting by "\n"
  3. Continue down the hierarchy until all pieces fit within chunk_size
  4. Merge small pieces back together up to chunk_size
```

### Implementation

```python
def recursive_chunk(text, chunk_size=500, overlap=50, separators=None):
    """Recursively split text using a hierarchy of separators."""
    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    if len(text) <= chunk_size:
        return [text]

    # Find the best separator
    separator = separators[-1]  # Default to finest granularity
    for sep in separators:
        if sep in text:
            separator = sep
            break

    # Split by chosen separator
    parts = text.split(separator) if separator else list(text)
    remaining_separators = separators[separators.index(separator) + 1:] if separator in separators else separators[1:]

    # Merge parts into chunks
    chunks = []
    current = ""

    for part in parts:
        candidate = current + separator + part if current else part

        if len(candidate) <= chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())

            # If part is still too big, recurse
            if len(part) > chunk_size and remaining_separators:
                sub_chunks = recursive_chunk(part, chunk_size, overlap, remaining_separators)
                chunks.extend(sub_chunks)
                current = ""
            else:
                current = part

    if current:
        chunks.append(current.strip())

    return chunks
```

### When to Use
- Most general-purpose RAG applications (this is the default recommendation)
- Mixed content documents
- When you want a good balance of simplicity and quality

---

## Strategy 4: Markdown / Structure-Aware Chunking

Use the document's own structure (headers, sections, HTML tags) as chunk boundaries.

### How It Works

```
# Chapter 1: Introduction        <-- Chunk boundary
Content about introduction...

## 1.1 Background                 <-- Chunk boundary
Background information...

## 1.2 Motivation                 <-- Chunk boundary
Why this matters...

# Chapter 2: Methods              <-- Chunk boundary
Methodology details...
```

Each section becomes a chunk, with the header hierarchy prepended as context.

### Implementation

```python
import re

def markdown_chunk(text, max_chunk_size=1500):
    """Split markdown by headers, preserving header hierarchy as context."""
    lines = text.split("\n")
    chunks = []
    current_headers = {}  # level -> header text
    current_content = []

    for line in lines:
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)

        if header_match:
            # Save current chunk
            if current_content:
                # Build header breadcrumb
                breadcrumb = " > ".join(
                    current_headers[k]
                    for k in sorted(current_headers.keys())
                    if k in current_headers
                )
                content = "\n".join(current_content).strip()
                if content:
                    if breadcrumb:
                        content = f"[Context: {breadcrumb}]\n\n{content}"
                    chunks.append(content)
                current_content = []

            # Update header hierarchy
            level = len(header_match.group(1))
            title = header_match.group(2)
            current_headers[level] = title
            # Clear lower-level headers
            for k in list(current_headers.keys()):
                if k > level:
                    del current_headers[k]

            current_content.append(line)
        else:
            current_content.append(line)

    # Don't forget last chunk
    if current_content:
        breadcrumb = " > ".join(
            current_headers[k]
            for k in sorted(current_headers.keys())
            if k in current_headers
        )
        content = "\n".join(current_content).strip()
        if content:
            if breadcrumb:
                content = f"[Context: {breadcrumb}]\n\n{content}"
            chunks.append(content)

    return chunks
```

### When to Use
- Well-structured documentation (technical docs, manuals)
- Markdown or HTML content
- Wiki pages
- Any content with clear hierarchical structure

### When NOT to Use
- Unstructured text (emails, chat logs)
- Documents without headers or sections

---

## Strategy 5: Semantic Chunking

Group text by semantic similarity -- sentences that are topically related stay together.

### How It Works

```
Step 1: Split into sentences
Step 2: Embed each sentence
Step 3: Compute similarity between consecutive sentences
Step 4: Find "breakpoints" where similarity drops significantly
Step 5: Group sentences between breakpoints into chunks

Similarity scores between consecutive sentences:
  S1-S2: 0.92  (same topic)
  S2-S3: 0.88  (same topic)
  S3-S4: 0.41  (TOPIC CHANGE - breakpoint!)
  S4-S5: 0.85  (same topic)
  S5-S6: 0.90  (same topic)
  S6-S7: 0.35  (TOPIC CHANGE - breakpoint!)
  S7-S8: 0.87  (same topic)

Result:
  Chunk 1: S1 + S2 + S3
  Chunk 2: S4 + S5 + S6
  Chunk 3: S7 + S8
```

### Implementation

```python
import numpy as np
from openai import OpenAI
import re

client = OpenAI()

def get_embeddings(texts, model="text-embedding-3-small"):
    """Get embeddings for a list of texts."""
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]

def cosine_sim(a, b):
    """Compute cosine similarity between two vectors."""
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def semantic_chunk(text, threshold=0.75, min_chunk_size=100):
    """Split text into semantically coherent chunks."""
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= 1:
        return [text]

    # Get embeddings for all sentences
    embeddings = get_embeddings(sentences)

    # Find breakpoints
    chunks = []
    current_chunk = [sentences[0]]

    for i in range(1, len(sentences)):
        similarity = cosine_sim(embeddings[i-1], embeddings[i])

        if similarity < threshold and len(" ".join(current_chunk)) >= min_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i]]
        else:
            current_chunk.append(sentences[i])

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
```

### When to Use
- Long documents covering multiple topics
- Research papers
- Meeting transcripts
- When topic coherence is critical

### When NOT to Use
- Short documents
- Already well-structured content (use structure-aware instead)
- When API costs for embedding every sentence are a concern

---

## Strategy 6: Agentic / Proposition-Based Chunking

Extract atomic propositions (single facts) from text, then group related propositions.

### How It Works

```
Input: "Albert Einstein was born in Ulm, Germany in 1879.
He developed the theory of relativity and won the Nobel Prize in 1921."

Propositions:
  P1: "Albert Einstein was born in Ulm, Germany."
  P2: "Albert Einstein was born in 1879."
  P3: "Albert Einstein developed the theory of relativity."
  P4: "Albert Einstein won the Nobel Prize."
  P5: "Albert Einstein won the Nobel Prize in 1921."

These are then grouped and indexed individually for maximum
retrieval precision.
```

### When to Use
- Knowledge-intensive applications requiring precise fact retrieval
- When each fact needs to be independently searchable
- Question-answering systems where precision matters more than context

---

## Strategy 7: Parent-Child (Small-to-Big) Chunking

Store small chunks for retrieval but return the larger parent chunk as context.

### How It Works

```
Original Document Section (Parent - 2000 chars):
  "Machine learning is a branch of AI... [full section]"

Child Chunks (for retrieval - 200 chars each):
  Child 1: "Machine learning is a branch of artificial intelligence..."
  Child 2: "Supervised learning uses labeled training data..."
  Child 3: "Common algorithms include decision trees, SVMs..."
  Child 4: "Deep learning is a subset using neural networks..."

At query time:
  1. Search matches Child 2 (most relevant small chunk)
  2. Return the Parent chunk as context (full section)
  3. LLM gets broader context while retrieval was precise
```

### Implementation

```python
def parent_child_chunk(text, parent_size=2000, child_size=400, child_overlap=50):
    """Create parent chunks with smaller child chunks for retrieval."""
    # Create parent chunks
    parents = recursive_chunk(text, chunk_size=parent_size, overlap=0)

    all_chunks = []
    for parent_idx, parent in enumerate(parents):
        # Create child chunks from each parent
        children = recursive_chunk(parent, chunk_size=child_size, overlap=child_overlap)

        for child_idx, child in enumerate(children):
            all_chunks.append({
                "child_text": child,           # Used for embedding/retrieval
                "parent_text": parent,          # Returned as context
                "parent_index": parent_idx,
                "child_index": child_idx,
            })

    return all_chunks
```

### When to Use
- When you need both precise retrieval AND rich context
- Long documents where broader context is important for understanding
- This is the recommended approach for many production RAG systems

---

## Chunk Size Guidelines by Use Case

| Use Case | Chunk Size | Overlap | Strategy | Rationale |
|----------|-----------|---------|----------|-----------|
| Q&A over docs | 300-500 tokens | 50-100 | Recursive | Focused answers need focused chunks |
| Summarization | 1000-2000 tokens | 100-200 | Structure-aware | Need broader context for summaries |
| Code docs | 500-1000 tokens | 50 | Structure-aware | Preserve function/class boundaries |
| Legal docs | 500-1000 tokens | 100-200 | Structure-aware | Preserve clause integrity |
| Chat/support | 200-500 tokens | 50 | Sentence-based | Quick, focused responses |
| Research papers | 500-1000 tokens | 100 | Semantic | Topic coherence matters |
| Knowledge base | 200-400 tokens | 50 | Proposition | Maximum precision for facts |

---

## Overlap Guidelines

```
PURPOSE OF OVERLAP:
  Ensures information at chunk boundaries isn't lost.
  Adjacent chunks share some content to maintain continuity.

RECOMMENDED OVERLAP:
  10-20% of chunk size is typical
  Chunk size 500 -> Overlap 50-100
  Chunk size 1000 -> Overlap 100-200

TOO LITTLE OVERLAP (< 5%):
  Risk of losing boundary information
  Sentences may be cut mid-thought

TOO MUCH OVERLAP (> 30%):
  Wasted storage and compute
  Redundant retrieval results
  Higher embedding costs
```

---

## Common Mistakes

### 1. Ignoring Document Structure
```
MISTAKE: Using fixed-size chunking on a structured document
RESULT:  Chunks split mid-section, headers separated from content
FIX:     Use structure-aware chunking for structured documents
```

### 2. Chunks Too Small
```
MISTAKE: Using 50-token chunks "for precision"
RESULT:  Chunks lack context, retrieval is noisy
FIX:     Minimum 200 tokens unless doing proposition-based chunking
```

### 3. Chunks Too Large
```
MISTAKE: Using 5000-token chunks "for context"
RESULT:  Retrieval returns irrelevant content mixed with relevant
         Wastes context window space
FIX:     Use parent-child strategy instead
```

### 4. No Overlap
```
MISTAKE: Using zero overlap between chunks
RESULT:  Information at boundaries is lost or split
FIX:     Use 10-20% overlap as default
```

### 5. One Strategy for All Documents
```
MISTAKE: Using the same chunking for PDFs, code, markdown, and emails
RESULT:  Poor retrieval quality for some document types
FIX:     Choose chunking strategy based on document type
```

---

## Testing Your Chunking Strategy

```python
def evaluate_chunking(chunks, test_queries, vector_store):
    """Simple evaluation: check if relevant chunks are retrieved."""
    results = []

    for query_info in test_queries:
        query = query_info["query"]
        expected_content = query_info["expected_in_result"]

        # Search
        search_results = vector_store.search(query, top_k=5)

        # Check if expected content appears in results
        found = any(
            expected_content.lower() in result["text"].lower()
            for result in search_results
        )

        results.append({
            "query": query,
            "found_expected": found,
            "top_score": search_results[0]["score"] if search_results else 0,
        })

    success_rate = sum(1 for r in results if r["found_expected"]) / len(results)
    print(f"Retrieval success rate: {success_rate:.1%}")
    return results
```

---

## Summary

1. **Start with recursive character splitting** -- it works well for most cases
2. **Use structure-aware chunking** for well-structured documents
3. **Consider semantic chunking** when topic coherence is critical
4. **Use parent-child strategy** when you need both precision and context
5. **Always include overlap** (10-20% of chunk size)
6. **Test your chunking** with real queries before deploying
7. **Different document types may need different strategies** -- it is acceptable to mix strategies in one system
