import requests
from bs4 import BeautifulSoup
import re

def clean_text(text, custom_filters=None):
    """
    Membersihkan teks dari tanda baca atau bagian tertentu yang tidak relevan.
    :param text: Teks asli
    :param custom_filters: Daftar pola regex untuk memfilter teks
    """
    # Hapus poin-poin dengan angka atau simbol tertentu
    text = re.sub(r"\d+\.", "", text)  # Hapus "1.", "2.", dll
    text = re.sub(r"[•●▪]", "", text)  # Hapus simbol bullet
    text = re.sub(r"\.{2,}", ".", text)  # Ganti titik lebih dari dua dengan satu titik
    text = re.sub(r"\s+", " ", text)  # Hapus spasi berlebihan
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

def get_website_content(url):
    """
    Mengambil dan membersihkan konten teks dari URL.
    Hanya teks dalam elemen <p> yang akan diambil dan dibersihkan.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memastikan permintaan berhasil
        soup = BeautifulSoup(response.content, 'html.parser')
        # Menggabungkan semua teks dari <p> tag
        raw_text = " ".join(p.text for p in soup.find_all('p'))
        # Membersihkan teks
        cleaned_text = clean_text(raw_text)
        return cleaned_text if cleaned_text else "Tidak ada teks yang ditemukan di halaman ini."
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

# Contoh penggunaan
# url = "https://example.com"
# content = get_website_content(url)
# print(content)
