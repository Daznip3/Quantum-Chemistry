import pandas as pd

def save_to_csv(records: list[dict], path: str):
    df = pd.DataFrame(records)
    df.to_csv(path, index=False)
