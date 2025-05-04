from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
model = SentenceTransformer("all-MiniLM-L6-v2")
query_embedding = model.encode([query])[0]
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5  # top-k similar chunks
) returns results['documents']     # list of top matching chunks
results['distances']     # cosine distances
results['ids']           # chunk IDs
results['metadatas']     # optional metadata (e.g., filename)
context = "\n\n".join(results['documents'][0])  # all top-5 chunks
