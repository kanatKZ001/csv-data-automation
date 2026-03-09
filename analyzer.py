import sys
import pandas as pd


def analyze_csv_file(input_file: str):
    """Analyze a CSV dataset and print useful statistics."""

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    print("\nDATASET OVERVIEW")
    print("----------------------------")

    rows, cols = df.shape
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")

    print("\nCOLUMN TYPES")
    print("----------------------------")
    print(df.dtypes)

    print("\nMISSING VALUES")
    print("----------------------------")
    print(df.isnull().sum())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        print("\nNUMERIC SUMMARY")
        print("----------------------------")
        print(df[numeric_cols].describe())

    categorical_cols = df.select_dtypes(include="object").columns

    if len(categorical_cols) > 0:
        print("\nTOP VALUES (CATEGORICAL)")
        print("----------------------------")

        for col in categorical_cols:
            print(f"\nColumn: {col}")
            print(df[col].value_counts().head(5))