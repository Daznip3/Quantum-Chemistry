import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_website(url: str) -> pd.DataFrame:
    """
    Парсит таблицу рецептов пива со страницы и возвращает DataFrame
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    if not table:
        print(f"⚠ No table found at {url}")
        return pd.DataFrame()

    headers = [th.text.strip() for th in table.find_all("th")]

    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.text.strip() for td in tr.find_all("td")]
        if cells:
            rows.append(cells)

    df = pd.DataFrame(rows, columns=headers)
    print(f"✔ Extracted {len(df)} rows from {url}")
    return df
