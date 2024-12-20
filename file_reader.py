from PyPDF2 import PdfReader
import docx

def read_pdf(file):
    """
    Membaca teks dari file PDF.
    """
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_txt(file):
    """
    Membaca teks dari file TXT.
    """
    return file.read().decode("utf-8")

def read_word(file):
    """
    Membaca teks dari file Word (DOCX).
    """
    doc = docx.Document(file)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text
