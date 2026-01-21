import requests
import pandas as pd
from io import StringIO


def extract_data(file_id: str) -> pd.DataFrame:
    url = "https://drive.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(url, params={"id": file_id})

    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            response = session.get(url, params={"id": file_id, "confirm": value})

    response.raise_for_status()

    df = pd.read_csv(
        StringIO(response.text),
        encoding="cp1251"   # 👈 ВАЖНО
    )

    print(f"✔ Extracted {len(df)} rows")
    return df
