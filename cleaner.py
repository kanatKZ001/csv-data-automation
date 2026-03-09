import sys
import pandas as pd


def clean_csv_file(input_file: str, output_file: str) -> str:
    """Clean a CSV file by removing duplicates, empty rows, and trimming text."""
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    df.columns = df.columns.str.strip()

    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].astype(str).str.strip()

    df = df.dropna(how="all")
    df = df.drop_duplicates()

    df.to_csv(output_file, index=False)
    return output_file