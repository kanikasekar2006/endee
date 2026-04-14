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


.
├── app.py # Main application (chat interface)
├── utils.py # Embedding + search logic
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/endee-project.git
cd endee-project
2. Create Virtual Environment
python -m venv .venv
3. Activate Environment

Windows (PowerShell):

.\.venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt

If requirements.txt is missing, install manually:

pip install PyPDF2 sentence-transformers numpy
▶️ How to Run
python app.py
💬 How It Works
Enter PDF file path
System reads and processes document
Data is stored in vector database
Ask questions in terminal
Get AI-based answers from document
🧪 Example Usage
Enter PDF file path: data/ml_notes.pdf

💬 Ask a question: What is machine learning?

📌 Answer:
Machine learning is a field of AI that enables systems to learn from data...
🧠 Technologies Used
Python
PyPDF2
SentenceTransformers
NumPy
Cosine Similarity
Vector Search (Endee-style concept)
📌 Future Improvements
Add real Endee vector database integration
Add FastAPI backend
Add web UI (React / Streamlit)
Support multiple file uploads
Use LLM (OpenAI / Llama) for better answers
👨‍💻 Author

Built as an AI/ML project using Endee for semantic search and RAG-based question answering.

⭐ Acknowledgement
Endee Vector Database
SentenceTransformers

---

# 🚀 WHAT YOU JUST BUILT 

Your project is now:

✔ RAG system  
✔ Semantic search engine  
✔ AI document chatbot  
✔ Uses embeddings + vector search  
