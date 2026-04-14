# 📚 AI Smart Document Assistant using Endee (RAG System)

## 🚀 Project Overview

This project is an AI-powered **Retrieval Augmented Generation (RAG)** system that allows users to upload a PDF document and ask questions based on its content.

The system:
- Extracts text from PDF files
- Splits text into chunks
- Converts chunks into embeddings using Sentence Transformers
- Stores embeddings in a simple vector database (Endee-like system)
- Retrieves the most relevant chunk based on user queries

---

## 🧠 Key Features

- 📄 PDF text extraction using PyPDF2  
- 🔍 Semantic search using embeddings  
- 🧠 SentenceTransformer (`all-MiniLM-L6-v2`) model  
- 📦 Simple in-memory vector database (Endee-style)  
- 💬 Interactive Q&A chatbot interface  
- ⚡ Fast similarity-based retrieval  

---

## 🏗️ System Architecture

1. User uploads PDF
2. Text is extracted using PyPDF2
3. Text is split into small chunks
4. Each chunk is converted into embeddings
5. Embeddings stored in vector database
6. User asks a question
7. Query is converted into embedding
8. Cosine similarity is calculated
9. Most relevant chunk is returned as answer

---

## 📁 Project Structure
