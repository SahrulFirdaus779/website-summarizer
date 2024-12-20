import streamlit as st
from scraper import get_website_content
from preprocess import preprocess_text
from summarizer import calculate_tfidf, summarize_text
from file_reader import read_pdf, read_txt, read_word
import nltk

# Unduh resource NLTK jika belum tersedia
nltk.download('punkt')
nltk.download('stopwords')

import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="saring-X", page_icon="📝", layout="wide")

# Judul Halaman dengan Desain
st.title("📝 **saring-X**: Aplikasi Ringkasan Cerdas")
# Deskripsi dengan Markdown yang Lebih Menarik
st.markdown(
    """
    **Selamat datang di _saring-X_!**  
    Saring-X adalah aplikasi canggih yang membantu Anda untuk meringkas teks dengan mudah dan cepat,  
    baik dari **URL** maupun **dokumen** (PDF, TXT, DOCX). Hanya dalam beberapa klik, Anda bisa mendapatkan **ringkasan**  
    yang jelas dan padat dalam bahasa **Indonesia** maupun **Inggris**.
    """
)

# Menambahkan Call-to-Action Button
st.button("Mulai Sekarang!", help="Klik untuk memulai merangkum teks Anda!")


# Pilihan Input dengan Tab
tab_url, tab_file = st.tabs(["🌐 URL", "📄 File"])

content = ""

with tab_url:
    st.subheader("📥 Masukkan URL")
    url = st.text_input("Masukkan URL:", placeholder="https://example.com")
    if url:
        with st.spinner("Mengambil konten dari URL..."):
            content = get_website_content(url)
            if content.startswith("Error"):
                st.error(content)
            else:
                st.success("Konten berhasil diambil!")

with tab_file:
    st.subheader("📤 Unggah Dokumen")
    uploaded_file = st.file_uploader(
        "Unggah dokumen (PDF, TXT, DOCX):", type=["pdf", "txt", "docx"], accept_multiple_files=False
    )
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]
        with st.spinner("Memproses file..."):
            if file_type == "pdf":
                content = read_pdf(uploaded_file)
            elif file_type == "txt":
                content = read_txt(uploaded_file)
            elif file_type == "docx":
                content = read_word(uploaded_file)
            else:
                st.error("Format file tidak didukung.")
        st.success("File berhasil diproses!")

# Proses dan Ringkasan
if content:
    st.subheader("🛠️ Proses Teks")
    sentences = nltk.sent_tokenize(content)
    if not sentences:
        st.error("Tidak ada teks yang dapat dirangkum.")
    else:
        with st.spinner("Memproses teks dan menghitung TF-IDF..."):
            # Preprocessing
            processed_sentences = [" ".join(preprocess_text(sentence)) for sentence in sentences]

            # Hitung TF-IDF
            vectorizer, tfidf_matrix = calculate_tfidf(processed_sentences)

        st.success("Proses selesai!")

        # Pilihan jumlah kalimat
        st.subheader("📋 Pengaturan Ringkasan")
        top_n = st.slider("Pilih jumlah kalimat untuk ringkasan:", min_value=1, max_value=10, value=3)
        
        # Buat Ringkasan
        summary = summarize_text(sentences, tfidf_matrix, top_n=top_n)

        # Tampilkan ringkasan
        st.subheader("📖 Ringkasan:")
        st.markdown(f"**Jumlah Kalimat:** {top_n}")
        st.write(summary)

        # Tombol untuk mengunduh hasil
        st.download_button(
            label="💾 Unduh Ringkasan",
            data=summary,
            file_name="ringkasan.txt",
            mime="text/plain"
        )
else:
    st.info("Masukkan URL atau unggah dokumen untuk memulai.")
