import pandas as pd

def extract_amount_unit(s):
    if pd.isna(s):
        return None, None
    parts = s.split(' ')
    if len(parts) == 2:
        try:
            return float(parts[0]), parts[1]
        except:
            return None, parts[1]
    return None, None

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # нормализуем имена колонок
    df.columns = [c.lower().strip().replace(' ', '_') for c in df.columns]

    # числовые колонки
    numeric_cols = ["og", "fg", "abv", "ibu", "color", "size(l)"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # разбиваем PrimingAmount на число и единицу
    df[["priming_amount_value", "priming_amount_unit"]] = df["primingamount"].apply(lambda x: pd.Series(extract_amount_unit(x)))

    # категориальные колонки
    df["style"] = df["style"].str.strip().str.title()
    df["brewmethod"] = df["brewmethod"].str.strip().str.title()
    df["primingmethod"] = df["primingmethod"].str.strip().str.title()

    # вычисляем Attenuation (%)
    df["attenuation"] = (df["og"] - df["fg"]) / df["og"] * 100

    # удаляем ненужные колонки
    df = df.drop(columns=["userid"])

    print("✔️ Transform completed")
    return df
