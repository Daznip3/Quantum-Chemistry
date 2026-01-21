import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:123@localhost:5432/mydb"
TABLE_NAME = "beer_recipes"

def get_engine():
    return create_engine(DB_URL)

def load_data(df: pd.DataFrame):
    """
    Загружает DataFrame в PostgreSQL
    """
    if df.empty:
        print("⚠ No data to load")
        return

    engine = get_engine()
    df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="replace",
        index=False,
        method="multi"
    )
    print(f"✔ Loaded {len(df)} rows into PostgreSQL ({TABLE_NAME})")
