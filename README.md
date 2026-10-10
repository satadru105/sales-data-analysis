 Sales Data Analysis

## Project Overview
This beginner-friendly data analysis project uses Python and Pandas to analyze sales records, handle missing data, remove duplicate rows, calculate key performance metrics, and generate a Markdown report.

## Objectives
- Load sales data from a CSV file.
- Explore rows, columns, data types, and missing values.
- Clean invalid and incomplete records.
- Calculate revenue, quantity sold, average sale value, and product performance.
- Generate an automated analysis report.

## Technologies Used
- Python
- Pandas
- CSV
- Markdown

## Project Structure
```text
Week3_Sales_Data_Analysis/
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
├── requirements.txt
├── README.md
└── screenshots/
```

## Installation
1. Install Python 3.
2. Open the project folder in VS Code.
3. Install dependencies:
   `python -m pip install -r requirements.txt`
4. Run the analysis:
   `python sales_analysis.py`

## Data Cleaning
The script removes duplicate rows, excludes missing product names and invalid quantities or prices, and recalculates revenue using quantity multiplied by unit price.

## Analysis Metrics
- Total revenue
- Total quantity sold
- Average sale value
- Highest and lowest sale values
- Revenue by product
- Product with the highest revenue and quantity sold

## Output
The script prints the analysis results and creates `analysis_report.md`, which contains the project overview, cleaning summary, metrics, product performance, insights, and conclusion.

## Testing
Test the CSV-loading process, data-cleaning rules, metric calculations, and report generation. Add screenshots of successful execution to the `screenshots/` directory.

## Learning Outcomes
This project demonstrates basic data analysis, CSV handling, data cleaning, aggregation, descriptive statistics, and report generation using Python and Pandas.