# chatbot.py
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.model_api import get_response_from_llm

# Load once when server starts
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="db", embedding_function=embedding)

def chat_with_bot(query):
    query_lower = query.lower()
    # Hardcoded CEO response logic
    if "ceo" in query_lower and "paves" in query_lower:
        return "Eada Sambi Reddy is the CEO of Paves Technologies India."


    docs = vectordb.similarity_search(query, k=2)  # reduce from 3 to 2

    # Optional: filter out large documents
    filtered = [doc for doc in docs if len(doc.page_content) < 1000]

    # Join text
    context = "\n\n".join(doc.page_content for doc in filtered)

    prompt = f"Answer the question using this info:\n\n{context}\n\nQuestion: {query}"
    return get_response_from_llm(prompt)
