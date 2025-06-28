from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.model_api import get_response_from_llm

def chat_with_bot(query):
    vectordb = Chroma(persist_directory="db", embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
    docs = vectordb.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = f"Answer the question using this info:\n\n{context}\n\nQuestion: {query}"
    return get_response_from_llm(prompt)
