# **saring-X: Website Summarizer**

**saring-X: Website Summarizer** adalah aplikasi berbasis Python yang dirancang untuk menghasilkan ringkasan singkat dari konten website atau dokumen. Aplikasi ini menggunakan algoritma **TF-IDF (Term Frequency-Inverse Document Frequency)** untuk menentukan kalimat-kalimat yang paling relevan dalam teks.

---

## **Fitur Utama**

- **Input URL atau Dokumen**:
  - Ambil teks dari halaman web menggunakan URL.
  - Mendukung pengunggahan file dokumen (PDF, Word, dan TXT).
- **Preprocessing Teks**:
  - Tokenisasi.
  - Penghapusan stop words (baik dalam bahasa Inggris maupun Indonesia).
  - Lemmatization.
- **Analisis TF-IDF**:
  - Menghitung skor TF-IDF untuk menentukan kalimat yang paling relevan.
- **Pembuatan Ringkasan**:
  - Menampilkan ringkasan berdasarkan skor TF-IDF tertinggi.
- **Antarmuka Pengguna Profesional**:
  - Dibangun menggunakan **Streamlit** dengan desain yang responsif dan ramah pengguna.

---

## **Cara Menggunakan**

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/website-summarizer.git
   cd website-summarizer
   ```

2. **Instal Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi**:
   ```bash
   streamlit run app.py
   ```

4. **Akses Aplikasi**:
   - Buka browser Anda dan akses aplikasi di **http://localhost:8501**.
   - Pilih metode input: URL atau unggah file dokumen.
   - Jika menggunakan URL, masukkan URL website untuk diambil kontennya.
   - Jika menggunakan dokumen, unggah file PDF, Word, atau TXT.
   - Aplikasi akan menghasilkan ringkasan dari konten yang dimasukkan.

---

## **Dependensi**

Aplikasi ini membutuhkan pustaka berikut:

- **`beautifulsoup4`**: Untuk mem-parsing HTML dan mengambil konten dari halaman web.
- **`nltk`**: Untuk preprocessing teks, seperti tokenisasi, penghapusan stop words, dan lemmatization.
- **`scikit-learn`**: Untuk menghitung skor TF-IDF.
- **`streamlit`**: Untuk membangun antarmuka pengguna yang interaktif.
- **`PyPDF2` dan `python-docx`**: Untuk membaca file PDF dan Word.

Instal semua pustaka dengan menjalankan:
```bash
pip install -r requirements.txt
```

---

## **Struktur Proyek**

```plaintext
website-summarizer/
|-- app.py              # File utama untuk menjalankan aplikasi
|-- scraper.py          # Modul untuk mengambil konten dari website
|-- preprocess.py       # Modul untuk preprocessing teks
|-- summarizer.py       # Modul untuk menghitung TF-IDF dan membuat ringkasan
|-- file_reader.py      # Modul untuk membaca file dokumen (PDF, Word, TXT)
|-- requirements.txt    # Daftar pustaka yang dibutuhkan
```

---

## **Lisensi**

Proyek ini dilisensikan di bawah **MIT License**. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan ulang kode ini dengan tetap mematuhi lisensi.

---

## **Kontributor**

Jika Anda ingin berkontribusi pada proyek ini, silakan kirimkan **pull request** atau laporkan masalah pada halaman **Issues** di repository ini.

---

## **Kontak**

Untuk pertanyaan lebih lanjut, silakan hubungi: 
- **Email**: your-email@example.com
- **GitHub**: [your-github-username](https://github.com/your-github-username)
