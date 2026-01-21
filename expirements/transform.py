import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Преобразует и очищает DataFrame
    """
    df = df.copy()

    # нормализуем имена колонок
    df.columns = [c.lower().strip().replace(' ', '_') for c in df.columns]

    # числовые колонки
    numeric_cols = ["партия", "нп", "кп", "алк", "ibu", "srm", "р.", "к.", "п."]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].str.replace('%', '').str.replace('л', '').str.replace(',', '.').str.strip()
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # категориальные колонки
    for col in ["рецепт", "стиль", "пивовар", "метод", "фото"]:
        if col in df.columns:
            df[col] = df[col].str.strip()

    print("✔ Transform completed")
    return df
