import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
# Unduh resource NLTK jika belum tersedia
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def preprocess_text(text, language="english"):
    # Tokenisasi
    tokens = word_tokenize(text.lower())
    # Pilih stopwords sesuai bahasa
    if language == "indonesian":
        stop_words = set(stopwords.words('indonesian'))
    else:
        stop_words = set(stopwords.words('english'))
    # Hapus stop words dan karakter non-alfanumerik
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]    
    return lemmatized_tokens
def calculate_tfidf(docs):
    """
    Menghitung TF-IDF untuk kumpulan dokumen.
    
    Parameter:
    - docs (list of str): Daftar dokumen dalam bentuk teks.
    
    Return:
    - vectorizer: Objek TF-IDF vectorizer.
    - tfidf_matrix: Matriks TF-IDF.
    """
    # Inisialisasi TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Hitung TF-IDF
    tfidf_matrix = vectorizer.fit_transform(docs)
    
    return vectorizer, tfidf_matrix












    """
    Melakukan preprocessing pada teks.
    - Tokenisasi
    - Stopword Removal
    - Lemmatization
    Parameter:
    - text (str): Teks yang akan diproses
    - language (str): Bahasa teks ("english" atau "indonesian")
    
    Return:
    - list: Token yang telah diproses
    """

# # Contoh Penggunaan
# if __name__ == "__main__":
#     # Daftar dokumen
#     texts = [
#         "I love programming in Python",
#         "Python programming is fun",
#         "I enjoy learning new programming languages"
#     ]
    
#     # Preprocessing dokumen
#     preprocessed_texts = [" ".join(preprocess_text(text)) for text in texts]
    
#     # Hitung TF-IDF
#     vectorizer, tfidf_matrix = calculate_tfidf(preprocessed_texts)
    
#     # Tampilkan fitur dan matriks TF-IDF
#     print("Fitur (Kata):", vectorizer.get_feature_names_out())
#     print("Matriks TF-IDF:")
#     print(tfidf_matrix.toarray())
