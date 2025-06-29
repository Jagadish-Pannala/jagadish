from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from app.model_api import get_response_from_llm

# Load once when server starts
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="db", embedding_function=embedding)

def chat_with_bot(query):
    query_lower = query.lower()

    if "ceo" in query_lower and "paves" in query_lower:
        return "Eada Sambi Reddy is the CEO of Paves Technologies India."

    docs = vectordb.similarity_search(query, k=2)

    filtered = [doc for doc in docs if len(doc.page_content) < 1000]

    if not filtered:
        return "Sorry, I couldn’t find an answer to that. Please try rephrasing your question."

    context = "\n\n".join(doc.page_content for doc in filtered)

    prompt = f"Answer the question using this info:\n\n{context}\n\nQuestion: {query}"
    return get_response_from_llm(prompt)
