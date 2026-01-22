import requests
from bs4 import BeautifulSoup

def fetch_cards(page: int):
    url = f"https://www.brewingnotes.ru/recipes/public?page={page}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
    return soup.select("div.card.bg-color")
