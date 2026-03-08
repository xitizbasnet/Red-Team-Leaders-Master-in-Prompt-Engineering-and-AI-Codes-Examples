# Vector Database Comparison Guide

## Module 05: Code and Examples

---

## Overview

This guide provides a detailed comparison of the most popular vector databases used in RAG (Retrieval-Augmented Generation) systems. Use this to select the right solution for your specific requirements.

---

## Quick Recommendation

| Your Situation | Recommended Database |
|---------------|---------------------|
| Learning / Prototyping | **ChromaDB** |
| Already using PostgreSQL, moderate scale | **pgvector** |
| Want zero-ops managed service | **Pinecone** |
| Need maximum performance, self-hosted | **Qdrant** |
| Billion-scale with GPU acceleration | **Milvus / Zilliz** |
| Need built-in vectorization | **Weaviate** |
| Embedding into a Python application | **FAISS** (library) |
| Need full-text + vector search | **Elasticsearch** with vector search |

---

## Detailed Comparison

### 1. Pinecone

```
Type:           Fully managed cloud service (SaaS)
Founded:        2019
Language:       Proprietary (cloud-only)
License:        Proprietary
Pricing:        Free tier + pay-as-you-go starting ~$70/month
```

**Strengths:**
- Zero infrastructure management -- truly serverless option available
- Excellent developer experience and documentation
- Built-in namespace isolation for multi-tenancy
- Hybrid search (sparse + dense vectors) with a single query
- SOC2 Type II compliant, enterprise-grade security
- Automatic scaling and high availability
- Strong Python and Node.js SDKs

**Limitations:**
- No self-hosted option -- cloud only
- Vendor lock-in risk
- Costs can grow significantly at scale
- Limited customization of indexing algorithms
- No raw SQL or familiar query interface

**Best For:**
Teams that want to focus on application logic without managing infrastructure. Enterprise deployments where compliance matters.

**Example Usage:**
```python
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_KEY")
index = pc.Index("my-index")

# Upsert vectors
index.upsert(
    vectors=[
        {"id": "doc1", "values": [0.1, 0.2, ...], "metadata": {"source": "file.pdf"}},
    ],
    namespace="documents"
)

# Query
results = index.query(
    vector=[0.1, 0.2, ...],
    top_k=5,
    namespace="documents",
    filter={"source": {"$eq": "file.pdf"}}
)
```

---

### 2. Weaviate

```
Type:           Open-source with managed cloud (WCS)
Founded:        2019
Language:       Go
License:        BSD-3-Clause
Pricing:        Free (self-hosted) / WCS starting ~$25/month
```

**Strengths:**
- Built-in vectorization modules (text2vec-openai, text2vec-transformers, etc.)
- GraphQL and REST APIs
- Hybrid search (BM25 + vector) built-in
- Generative search module (ask questions, get generated answers)
- Multi-tenancy support
- Both self-hosted and managed options
- Active community and extensive documentation

**Limitations:**
- Memory-intensive (stores everything in memory by default)
- GraphQL can have a learning curve
- Module system adds complexity
- Can be slower than Rust-based alternatives

**Best For:**
Teams wanting a flexible, feature-rich solution with built-in AI capabilities. Good when you want the database to handle embedding generation.

**Example Usage:**
```python
import weaviate

client = weaviate.connect_to_local()

collection = client.collections.get("Documents")

# Add with automatic vectorization
collection.data.insert(
    properties={"content": "RAG combines retrieval with generation", "source": "guide.pdf"},
)

# Semantic search
response = collection.query.near_text(
    query="How does RAG work?",
    limit=5
)
```

---

### 3. ChromaDB

```
Type:           Open-source, embeddable
Founded:        2022
Language:        Python (with Rust backend)
License:        Apache 2.0
Pricing:        Free (open-source)
```

**Strengths:**
- Extremely simple API -- get started in 5 lines of code
- Embeddable (runs in-process, no separate server needed)
- Python-native with first-class support
- Built-in embedding functions (OpenAI, HuggingFace, etc.)
- Persistent and in-memory modes
- Great for prototyping, education, and small-medium projects
- Active development and improving rapidly

**Limitations:**
- Not designed for massive scale (millions of vectors is the practical limit)
- Limited production features (no built-in replication, backup)
- Fewer advanced features compared to Pinecone or Weaviate
- Newer project, less battle-tested in large deployments
- Limited filtering capabilities compared to alternatives

**Best For:**
Learning, prototyping, small to medium projects, embedding into Python applications where simplicity matters most.

**Example Usage:**
```python
import chromadb

client = chromadb.PersistentClient(path="./my_db")
collection = client.get_or_create_collection("documents")

# Add documents (auto-embeds with default model)
collection.add(
    documents=["RAG combines retrieval with generation"],
    metadatas=[{"source": "guide.pdf"}],
    ids=["doc1"]
)

# Query
results = collection.query(
    query_texts=["How does RAG work?"],
    n_results=5
)
```

---

### 4. Qdrant

```
Type:           Open-source with managed cloud
Founded:        2021
Language:        Rust
License:        Apache 2.0
Pricing:        Free (self-hosted) / Cloud starting ~$25/month
```

**Strengths:**
- Extremely fast -- written in Rust for maximum performance
- Rich filtering capabilities with payload indexing
- Named vectors (multiple vectors per point)
- Quantization support (scalar, product, binary) for cost reduction
- gRPC and REST APIs
- Excellent documentation
- Good balance of features and performance
- Snapshot and backup support

**Limitations:**
- Smaller community than Pinecone or Weaviate
- Fewer built-in integrations (no auto-vectorization)
- Requires more manual setup compared to Pinecone

**Best For:**
Performance-critical production applications. Teams that want a fast, reliable, open-source solution with good filtering.

**Example Usage:**
```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient(path="./qdrant_db")

# Create collection
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

# Add vectors
client.upsert(
    collection_name="documents",
    points=[
        PointStruct(id=1, vector=[0.1, 0.2, ...],
                    payload={"source": "guide.pdf", "content": "..."})
    ]
)

# Search with filtering
results = client.search(
    collection_name="documents",
    query_vector=[0.1, 0.2, ...],
    query_filter={"must": [{"key": "source", "match": {"value": "guide.pdf"}}]},
    limit=5
)
```

---

### 5. pgvector (PostgreSQL Extension)

```
Type:           PostgreSQL extension
Founded:        2021
Language:        C
License:        PostgreSQL License (permissive)
Pricing:        Free (open-source, uses your existing PostgreSQL)
```

**Strengths:**
- Leverages your existing PostgreSQL infrastructure
- Familiar SQL interface
- ACID transactions -- combine vector search with relational operations
- No new technology to learn for SQL-experienced teams
- Supports both ivfflat and HNSW indexes
- Can join vector results with relational tables
- Available on major cloud providers (AWS RDS, Cloud SQL, etc.)

**Limitations:**
- Performance is lower than purpose-built vector databases
- Not designed for billion-scale vector search
- Index building can be slow for large datasets
- Memory management not optimized for vector workloads
- Limited ANN algorithm options

**Best For:**
Teams already using PostgreSQL who need moderate-scale vector search without adding new infrastructure.

**Example Usage:**
```sql
-- Enable extension
CREATE EXTENSION vector;

-- Create table with vector column
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    source VARCHAR(255),
    embedding vector(1536)
);

-- Create HNSW index
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);

-- Insert
INSERT INTO documents (content, source, embedding)
VALUES ('RAG combines retrieval...', 'guide.pdf', '[0.1, 0.2, ...]');

-- Search
SELECT content, source, 1 - (embedding <=> '[0.1, 0.2, ...]') AS similarity
FROM documents
ORDER BY embedding <=> '[0.1, 0.2, ...]'
LIMIT 5;
```

---

### 6. Milvus / Zilliz

```
Type:           Open-source (Milvus) with managed cloud (Zilliz)
Founded:        2019
Language:        Go, C++
License:        Apache 2.0
Pricing:        Free (self-hosted) / Zilliz Cloud from $0 (free tier)
```

**Strengths:**
- Designed for billion-scale vector search
- Multiple index types (IVF, HNSW, DiskANN, GPU-IVF)
- GPU acceleration support
- Partition and shard support for distributed deployments
- Mature and battle-tested (used by many large companies)
- Hybrid search (dense + sparse)
- Schema enforcement

**Limitations:**
- Complex deployment for self-hosted (Kubernetes recommended)
- Steeper learning curve
- Higher resource requirements than lighter alternatives
- Overkill for small-medium projects

**Best For:**
Large-scale deployments with billions of vectors, GPU-accelerated search, enterprise environments.

---

### 7. FAISS (Facebook AI Similarity Search)

```
Type:           Library (not a database)
Founded:        2017
Language:        C++ with Python bindings
License:        MIT
Pricing:        Free (open-source)
```

**Strengths:**
- Blazing fast search (optimized C++ implementation)
- GPU support for acceleration
- Multiple index types (Flat, IVF, HNSW, PQ, etc.)
- Battle-tested at Meta scale
- No server overhead -- runs in-process
- Excellent for research and custom applications

**Limitations:**
- Library, NOT a database (no built-in persistence, CRUD, metadata)
- No filtering by metadata
- No built-in API or server
- Requires custom code for persistence and management
- Not designed for concurrent writes

**Best For:**
Research, embedding into custom applications, when you need maximum control and performance without database overhead.

---

## Performance Benchmarks Summary

Note: Benchmarks vary significantly by dataset, hardware, and configuration. These are approximate relative comparisons.

```
QUERY LATENCY (lower is better):
  FAISS (GPU)    ████                     ~1ms
  Qdrant         ██████                   ~3ms
  Milvus         ████████                 ~5ms
  Pinecone       ██████████               ~8ms
  Weaviate       ████████████             ~10ms
  pgvector       ██████████████████       ~20ms
  ChromaDB       ████████████████████     ~25ms

INDEXING SPEED (higher is better):
  FAISS          ████████████████████     Fastest
  Qdrant         ████████████████         Very Fast
  Milvus         ██████████████           Fast
  Pinecone       ████████████             Good
  Weaviate       ██████████               Good
  ChromaDB       ████████                 Moderate
  pgvector       ██████                   Moderate

EASE OF USE (higher is better):
  ChromaDB       ████████████████████     Simplest
  Pinecone       ████████████████████     Very Easy
  pgvector       ██████████████████       Easy (if you know SQL)
  Qdrant         ████████████████         Easy
  Weaviate       ██████████████           Moderate
  Milvus         ████████                 Complex
  FAISS          ██████                   Requires custom code
```

---

## Decision Matrix by Scale

| Scale | Recommended | Why |
|-------|------------|-----|
| < 10K vectors | ChromaDB or pgvector | Simplest setup, performance doesn't matter at this scale |
| 10K - 1M vectors | Qdrant, Weaviate, or Pinecone | Good balance of features and performance |
| 1M - 100M vectors | Qdrant Cloud, Pinecone, or Milvus | Need proper indexing and infrastructure |
| 100M - 1B vectors | Milvus/Zilliz or Pinecone Enterprise | Need distributed architecture |
| > 1B vectors | Milvus/Zilliz with GPU | Need GPU acceleration and sharding |

---

## Framework Integration Support

| Framework | Pinecone | Weaviate | ChromaDB | Qdrant | pgvector | Milvus |
|-----------|:--------:|:--------:|:--------:|:------:|:--------:|:------:|
| LangChain | Yes | Yes | Yes | Yes | Yes | Yes |
| LlamaIndex | Yes | Yes | Yes | Yes | Yes | Yes |
| Haystack | Yes | Yes | Yes | Yes | Yes | Yes |
| Semantic Kernel | Yes | Yes | Yes | Yes | Partial | Partial |
| Spring AI | Yes | Yes | Yes | Yes | Yes | Yes |

All major vector databases have good integration with the popular RAG frameworks.

---

## Total Cost of Ownership (12 months, 1M vectors)

```
ChromaDB (self-hosted):     ~$50/month   (minimal compute)
pgvector (existing PG):     ~$0 extra    (uses existing DB)
Qdrant (self-hosted):       ~$100/month  (dedicated instance)
Qdrant Cloud:               ~$150/month  (managed)
Weaviate Cloud:             ~$200/month  (managed)
Pinecone (Serverless):      ~$100/month  (pay-per-use)
Pinecone (Standard):        ~$250/month  (dedicated pods)
Milvus (self-hosted):       ~$200/month  (Kubernetes cluster)
Zilliz Cloud:               ~$200/month  (managed Milvus)
```

*Costs are approximate and vary by region, configuration, and query volume.*

---

## Migration Considerations

If you need to switch vector databases later:

1. **Embeddings are portable**: Your vectors work with any database (they are just arrays of numbers)
2. **Metadata schemas may differ**: Each DB has slightly different metadata capabilities
3. **Index configurations differ**: HNSW parameters, quantization settings are not portable
4. **Use abstraction layers**: LangChain and LlamaIndex abstract the vector store, making migration easier
5. **Plan for re-indexing time**: Large collections may take hours to re-index in a new database

---

## Final Recommendation

For most teams starting with RAG:

1. **Start with ChromaDB** for development and prototyping
2. **Move to Qdrant or Pinecone** for production
3. **Consider pgvector** if you are already invested in PostgreSQL
4. **Use Milvus** only if you truly need billion-scale search

The most important factor is usually **not** the database itself but the quality of your **embeddings, chunking strategy, and retrieval logic**.
