from docx import Document

def extract_text():
    doc = Document("app\\company.docx")  # <-- use quotes
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

