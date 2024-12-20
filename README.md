# Website Summarizer

Website Summarizer adalah aplikasi berbasis Python yang digunakan untuk menghasilkan ringkasan dari konten sebuah website. Aplikasi ini menggunakan **TF-IDF** untuk menentukan kalimat-kalimat penting dari konten web.

## Fitur
- Ambil konten dari halaman web menggunakan URL.
- Lakukan preprocessing teks seperti tokenisasi, penghapusan stop words, dan lemmatization.
- Hitung skor **TF-IDF** untuk menentukan kalimat paling relevan.
- Hasilkan ringkasan singkat dari konten website.
- Antarmuka interaktif menggunakan **Streamlit**.

## Cara Menggunakan
1. **Clone repository** ini ke lokal Anda:
   ```bash
   git clone https://github.com/username/website-summarizer.git
   cd website-summarizer

Instal dependensi yang diperlukan:

pip install -r requirements.txt

Jalankan aplikasi menggunakan Streamlit:
streamlit run app.py

Akses aplikasi melalui browser di http://localhost:8501. Masukkan URL website pada input yang disediakan, dan aplikasi akan menghasilkan ringkasan konten.

Dependensi
* beautifulsoup4: Untuk mem-parsing HTML dan mengambil konten dari website.
* nltk: Untuk preprocessing teks seperti tokenisasi, penghapusan stop words, dan lemmatization.
* scikit-learn: Untuk menghitung TF-IDF.
* streamlit: Untuk membangun antarmuka pengguna.
