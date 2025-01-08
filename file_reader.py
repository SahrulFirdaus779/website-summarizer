from PyPDF2 import PdfReader
import docx
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
# 1. Fungsi untuk membaca PDF
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
# 2. Fungsi untuk membaca file TXT
def read_txt(file):
    return file.read().decode("utf-8")
# 3. Fungsi untuk membaca file Word
def read_word(file):
    doc = docx.Document(file)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text
# 4. Fungsi untuk membersihkan teks
def clean_text(text, custom_filters=None):
    # Hapus poin-poin dengan angka atau simbol tertentu
    text = re.sub(r"\d+\.", "", text)  # Hapus "1.", "2.", dll
    text = re.sub(r"[•●▪]", "", text)  # Hapus simbol bullet
    text = re.sub(r"\.{2,}", ".", text)  # Ganti titik lebih dari dua dengan satu titik
    text = re.sub(r"\s+", " ", text)  # Hapus spasi berlebihan
    # Tambahan filter
    text = re.sub(r"http\S+", "", text)  # Hapus URL
    text = re.sub(r"\[[^\]]*\]", "", text)  # Hapus teks dalam tanda kurung siku [contoh]
    text = re.sub(r"\([^\)]*\)", "", text)  # Hapus teks dalam tanda kurung biasa (contoh)
    text = re.sub(r"[^a-zA-Z0-9.,!?'\s]", "", text)  # Hapus karakter non-alfanumerik kecuali tanda baca dasar
    text = re.sub(r"(?<=\s)\d+(?=\s)", "", text)  # Hapus angka yang berdiri sendiri
    text = re.sub(r"\b\w{1,2}\b", "", text)  # Hapus kata dengan panjang 1-2 huruf
    text = re.sub(r"\s+", " ", text)  # Normalisasi spasi kembali
    # Terapkan filter kustom jika ada
    if custom_filters:
        for pattern in custom_filters:
            text = re.sub(pattern, "", text)
    return text.strip()
# 5. Fungsi untuk menghitung TF-IDF dan membuat ringkasan
def summarize_text(sentences, top_n=3):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    ranked_sentences = [sentences[i] for i in scores.argsort()[-top_n:][::-1]]
    return " ".join(ranked_sentences)
# 6. Workflow untuk membuat ringkasan dari file
def process_and_summarize(file, file_type, top_n=3, custom_filters=None):
    if file_type == "pdf":
        text = read_pdf(file)
    elif file_type == "txt":
        text = read_txt(file)
    elif file_type == "word":
        text = read_word(file)
    else:
        raise ValueError("Unsupported file type!")
    # Bersihkan teks
    clean = clean_text(text, custom_filters)

    # Pisahkan teks menjadi kalimat
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", clean)
    # Buat ringkasan
    summary = summarize_text(sentences, top_n=top_n)
    return summary
# # Contoh Penggunaan
# if __name__ == "__main__":
#     # Ganti '

    """
    Membersihkan teks dari tanda baca atau bagian tertentu yang tidak relevan.
    :param text: Teks asli
    :param custom_filters: Daftar pola regex untuk memfilter teks
    """
    """
    Membuat ringkasan berdasarkan skor TF-IDF.
    :param sentences: Daftar kalimat
    :param top_n: Jumlah kalimat ringkasan
    """
    """
    Workflow utama untuk membaca, memfilter, dan merangkum teks dari berbagai jenis file.
    :param file: File input
    :param file_type: Jenis file ('pdf', 'txt', 'word')
    :param top_n: Jumlah kalimat dalam ringkasan
    :param custom_filters: Daftar pola regex untuk memfilter teks
    """