import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Menggabungkan semua teks dari <p> tag
        text = " ".join(p.text for p in soup.find_all('p'))
        return text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
