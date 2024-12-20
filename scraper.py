import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    """
    Mengambil konten teks dari URL.
    Hanya teks dalam elemen <p> yang akan diambil.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memastikan permintaan berhasil
        soup = BeautifulSoup(response.content, 'html.parser')
        # Menggabungkan semua teks dari <p> tag
        text = " ".join(p.text for p in soup.find_all('p'))
        return text if text else "Tidak ada teks yang ditemukan di halaman ini."
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
