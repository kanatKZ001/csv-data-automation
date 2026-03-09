import argparse
import os

from merger import merge_csv_files
from cleaner import clean_csv_file
from analyzer import analyze_csv_file
from visualizer import generate_bar_chart, generate_histogram


def parse_arguments():
    parser = argparse.ArgumentParser(description="CSV Data Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    merge_parser = subparsers.add_parser("merge", help="Merge all CSV files in a folder")
    merge_parser.add_argument("input_folder", help="Path to folder containing CSV files")
    merge_parser.add_argument(
        "--output",
        default="output/merged.csv",
        help="Path for merged output CSV"
    )

    clean_parser = subparsers.add_parser("clean", help="Clean a CSV file")
    clean_parser.add_argument("input_file", help="Path to CSV file to clean")
    clean_parser.add_argument(
        "--output",
        default="output/cleaned.csv",
        help="Path for cleaned output CSV"
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze a CSV dataset"
    )
    analyze_parser.add_argument(
        "input_file",
        help="Path to CSV file to analyze"
    )

    chart_parser = subparsers.add_parser(
        "chart",
        help="Generate chart from a CSV dataset"
    )
    chart_parser.add_argument(
        "input_file",
        help="Path to CSV file"
    )
    chart_parser.add_argument(
        "--kind",
        choices=["bar", "hist"],
        required=True,
        help="Type of chart to generate"
    )
    chart_parser.add_argument(
        "--column",
        required=True,
        help="Column name to visualize"
    )
    chart_parser.add_argument(
        "--output",
        default="output/charts/chart.png",
        help="Path to save chart image"
    )

    return parser.parse_args()


def ensure_output_folder():
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/charts", exist_ok=True)


def main():
    args = parse_arguments()
    ensure_output_folder()

    if args.command == "merge":
        output_path = merge_csv_files(args.input_folder, args.output)
        print(f"Merged file saved to: {output_path}")

    elif args.command == "clean":
        output_path = clean_csv_file(args.input_file, args.output)
        print(f"Cleaned file saved to: {output_path}")

    elif args.command == "analyze":
        analyze_csv_file(args.input_file)

    elif args.command == "chart":
        if args.kind == "bar":
            output_path = generate_bar_chart(args.input_file, args.column, args.output)
        else:
            output_path = generate_histogram(args.input_file, args.column, args.output)

        print(f"Chart saved to: {output_path}")


if __name__ == "__main__":
    main()