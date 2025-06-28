# build_db.py
from app.doc_parser import extract_text
from app.embedder import create_vector_store

text = extract_text()  # Will load from app/company.docx
create_vector_store(text)  # Builds and persists vector DB in 'db/'
