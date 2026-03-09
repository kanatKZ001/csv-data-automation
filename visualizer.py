import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


def generate_bar_chart(input_file: str, column: str, output_file: str) -> str:
    """Generate bar chart for a categorical column."""
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    if column not in df.columns:
        print(f"Error: column '{column}' not found in dataset.")
        sys.exit(1)

    counts = df[column].astype(str).str.strip().value_counts().head(10)

    if counts.empty:
        print(f"Error: no usable data found in column '{column}'.")
        sys.exit(1)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    plt.figure(figsize=(10, 6))
    counts.plot(kind="bar")
    plt.title(f"Top Values in '{column}'")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    return output_file


def generate_histogram(input_file: str, column: str, output_file: str) -> str:
    """Generate histogram for a numeric column."""
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    if column not in df.columns:
        print(f"Error: column '{column}' not found in dataset.")
        sys.exit(1)

    series = pd.to_numeric(df[column], errors="coerce").dropna()

    if series.empty:
        print(f"Error: column '{column}' does not contain valid numeric data.")
        sys.exit(1)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.hist(series, bins=10)
    plt.title(f"Distribution of '{column}'")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    return output_file