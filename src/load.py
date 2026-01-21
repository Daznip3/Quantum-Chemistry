import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


DB_URL = "postgresql://postgres:123@localhost:5432/postgres"

def get_engine() -> Engine:
    return create_engine(DB_URL)


def load_data(df: pd.DataFrame):
    """
    Load DataFrame into PostgreSQL
    """
    csv_path = "beer_recipes_output.csv"
    df.to_csv(csv_path, index=False, mode="a", header=not pd.io.common.file_exists(csv_path))
    print(f"✔️ Saved {len(df)} rows to CSV ({csv_path})")


    engine = get_engine()

    df.to_sql(
        name="etl_table",
        con=engine,
        if_exists="replace",
        index=False,
        method="multi"
    )

    print(f"✔️ Loaded {len(df)} rows into PostgreSQL (table: etl_table)")
