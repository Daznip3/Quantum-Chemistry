import argparse
from extract import extract_data
from transform import transform_data
from load import load_data


def run_etl(file_id: str):
    print("▶ Extract step")
    df = extract_data(file_id)

    print("▶ Transform step")
    df_transformed = transform_data(df)

    print("▶ Load step")
    load_data(df_transformed)

    print("✅ ETL pipeline finished successfully")


def main():
    parser = argparse.ArgumentParser(description="Simple ETL pipeline")
    parser.add_argument(
        "--file-id",
        required=True,
        help="Google Drive file ID of CSV file"
    )

    args = parser.parse_args()
    run_etl(args.file_id)


if __name__ == "__main__":
    main()
