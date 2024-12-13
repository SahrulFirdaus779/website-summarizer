import streamlit as st
from scraper import get_website_content
from preprocess import preprocess_text
from summarizer import calculate_tfidf, summarize_text
import nltk

# Pastikan data NLTK tersedia
nltk.download('punkt')

# Judul aplikasi
st.title("Website Summarizer")
st.subheader("Meringkas konten dari sebuah website menggunakan TF-IDF")

# Input URL dari pengguna
url = st.text_input("Masukkan URL Website:")

if st.button("Buat Ringkasan"):
    if not url:
        st.warning("Harap masukkan URL terlebih dahulu.")
    else:
        st.info("Mengambil konten dari website...")
        content = get_website_content(url)
        
        if content.startswith("Error"):
            st.error(content)
        else:
            st.success("Konten berhasil diambil!")
            st.write("**Konten Asli (terpotong):**")
            st.text_area("Konten Asli", content[:500], height=200)

            # Proses ringkasan
            st.info("Memproses teks...")
            sentences = nltk.sent_tokenize(content)
            processed_sentences = [" ".join(preprocess_text(sentence)) for sentence in sentences]
            _, tfidf_matrix = calculate_tfidf(processed_sentences)
            summary = summarize_text(sentences, tfidf_matrix)
            
            # Tampilkan ringkasan
            st.write("**Ringkasan Konten:**")
            st.text_area("Ringkasan", summary, height=150)
