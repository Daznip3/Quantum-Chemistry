from extract import extract_website
from transform import transform_data
from load import load_data
import pandas as pd

def main():
    urls = [
        "https://xn--90aoy.xn--p1ai/beer_recipes/bjcp_2015"
    ]

    all_dfs = []

    for url in urls:
        df = extract_website(url)
        if not df.empty:
            all_dfs.append(df)

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        transformed_df = transform_data(combined_df)
        load_data(transformed_df)
    else:
        print("⚠ No data extracted")

if __name__ == "__main__":
    main()
