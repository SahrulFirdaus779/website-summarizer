from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def calculate_tfidf(sentences):
    """
    Menghitung TF-IDF untuk daftar kalimat.
    Parameter:
    - sentences (list): Daftar kalimat
    
    Return:
    - vectorizer: Objek TfidfVectorizer
    - tfidf_matrix: Matriks TF-IDF
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    return vectorizer, tfidf_matrix

def summarize_text(sentences, tfidf_matrix, top_n=3):
    """
    Membuat ringkasan berdasarkan skor TF-IDF.
    
    Parameter:
    - sentences (list): Daftar kalimat asli
    - tfidf_matrix (sparse matrix): Matriks TF-IDF
    - top_n (int): Jumlah kalimat untuk ringkasan
    
    Return:
    - str: Ringkasan teks
    """
    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    ranked_sentences = [sentences[i] for i in scores.argsort()[-top_n:][::-1]]
    return " ".join(ranked_sentences)
