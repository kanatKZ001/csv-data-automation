import os
import sys
import pandas as pd


def merge_csv_files(input_folder: str, output_file: str) -> str:
    """Merge all CSV files from a folder into one CSV file."""
    if not os.path.isdir(input_folder):
        print(f"Error: folder not found: {input_folder}")
        sys.exit(1)

    csv_files = [
        os.path.join(input_folder, file_name)
        for file_name in os.listdir(input_folder)
        if file_name.lower().endswith(".csv")
    ]

    if not csv_files:
        print(f"Error: no CSV files found in folder: {input_folder}")
        sys.exit(1)

    dataframes = []

    for file_path in csv_files:
        try:
            df = pd.read_csv(file_path)
            df["source_file"] = os.path.basename(file_path)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            sys.exit(1)

    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df.to_csv(output_file, index=False)

    return output_file