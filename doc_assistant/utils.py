from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store embeddings in memory (simple Endee-like usage)
vector_db = []
documents = []

def add_document(text):
    chunk_size = 300   # smaller = better answers
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        
        embedding = model.encode(chunk)
        vector_db.append(embedding)
        documents.append(chunk)

def search(query):
    query_embedding = model.encode(query)
    
    similarities = []
    for emb in vector_db:
        sim = np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb))
        similarities.append(sim)

    best_match_index = np.argmax(similarities)
    return documents[best_match_index]