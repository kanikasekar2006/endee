import PyPDF2
import os
from utils import add_document, search

def extract_text_from_pdf(file_path):
    text = ""

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text


def main():
    print("📄 AI Smart Document Assistant (Endee-based RAG)\n")

    pdf_path = input("Enter PDF file path: ").strip()

    # ✅ FIX 1: empty input check
    if not pdf_path:
        print("❌ No file path provided!")
        return

    # ✅ FIX 2: file existence check
    if not os.path.exists(pdf_path):
        print("❌ File not found:", pdf_path)
        return

    print("\n⏳ Reading document...")
    text = extract_text_from_pdf(pdf_path)

    print("📥 Storing in vector database...")
    add_document(text)

    while True:
        query = input("\n💬 Ask a question (or type 'exit'): ").strip()

        if query.lower() == 'exit':
            print("👋 Exiting...")
            break

        if not query:
            print("❌ Please enter a question!")
            continue

        result = search(query)
        print("\n📌 Answer:\n", result)


if __name__ == "__main__":
    main()