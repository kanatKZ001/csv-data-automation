# CSV Data Automation Tool

A Python command-line tool for **automating CSV data workflows** such as merging datasets, cleaning messy data, analyzing datasets, and generating charts.

This project demonstrates practical **data automation, cleaning, analysis, and visualization using Python and pandas**.

---

## Features

* Merge multiple CSV files into a single dataset
* Clean messy CSV data:

  * remove empty rows
  * remove duplicates
  * trim text columns
* Analyze datasets:

  * dataset shape
  * column types
  * missing values
  * numeric statistics
  * most common categorical values
* Generate charts:

  * bar charts for categorical columns
  * histograms for numeric columns
* Command-line interface with subcommands

---

## Project Structure

```text
csv-data-automation
│
├── main.py           # CLI entry point
├── merger.py         # CSV merging logic
├── cleaner.py        # Data cleaning functions
├── analyzer.py       # Dataset analysis
├── visualizer.py     # Chart generation
│
├── sample_data
│   ├── sales_january.csv
│   ├── sales_february.csv
│   └── sales_march.csv
│
├── output
│   └── charts
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/csv-data-automation.git
cd csv-data-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Example Dataset

Example CSV format:

```csv
date,product,category,amount,customer
2026-01-03,Laptop,Electronics,1200,Alice
2026-01-05,Mouse,Electronics,25,Bob
2026-01-08,Chair,Furniture,180,Charlie
```

---

## Usage

### Merge multiple CSV files

```bash
python main.py merge sample_data
```

Output:

```
output/merged.csv
```

---

### Clean dataset

```bash
python main.py clean output/merged.csv
```

Output:

```
output/cleaned.csv
```

---

### Analyze dataset

```bash
python main.py analyze output/cleaned.csv
```

Example output:

```
DATASET OVERVIEW
Rows: 12
Columns: 5

COLUMN TYPES
date        object
product     object
category    object
amount      int64
customer    object

MISSING VALUES
date        0
product     0
category    0
amount      0
customer    0
```

---

### Generate bar chart

```bash
python main.py chart output/cleaned.csv --kind bar --column category
```

---

### Generate histogram

```bash
python main.py chart output/cleaned.csv --kind hist --column amount
```

Charts are saved inside:

```
output/charts/
```

---

## Technologies Used

* Python
* pandas
* matplotlib
* argparse

---

## Possible Improvements

Future enhancements could include:

* Excel support
* automatic report generation
* interactive dashboards
* data validation rules
* batch processing pipelines

---

## Author

Kanat Zhumatov

Computer Science student interested in **Python automation, data analysis, and building practical developer tools**.
