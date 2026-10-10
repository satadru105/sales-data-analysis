# Sales Data Analysis Report

## 1. Project Overview

This project uses Python and Pandas to clean and analyze
a sample sales dataset and identify useful business insights.

## 2. Data Cleaning

- Original rows: 12
- Exact duplicate rows removed: 0
- Valid rows analyzed: 10
- Missing product names were excluded.
- Invalid or missing quantities were excluded.
- Missing or invalid unit prices were excluded.
- Revenue was recalculated using Quantity × Unit_Price.

## 3. Key Performance Metrics

| Metric | Result |
|---|---:|
| Total revenue | Rs. 262,800.00 |
| Total units sold | 42 |
| Average sale value | Rs. 26,280.00 |
| Highest sale | Rs. 90,000.00 |
| Lowest sale | Rs. 3,000.00 |
| Valid sales records | 10 |

## 4. Product Performance

**Top product by revenue:** Laptop

**Revenue from this product:** Rs. 180,000.00

**Product with most units sold:** Mouse

**Units sold:** 24

### Revenue by Product

| Product | Revenue (Rs.) |
|---|---:|
| Laptop | 180,000.00 |
| Monitor | 60,000.00 |
| Mouse | 12,000.00 |
| Keyboard | 10,800.00 |

## 5. Business Insights

- Total recorded revenue is Rs. 262,800.00.
- Laptop generated the highest product revenue.
- Mouse had the highest total quantity sold.
- Average sale value was Rs. 26,280.00.

## 6. Conclusion

Pandas helped load, clean, group, and summarize sales records.
These results can help a business understand product performance
and make more informed inventory and sales decisions.

## 7. Tools Used

- Python
- Pandas
- CSV
- Markdown

## 8. Validation

The report was generated from the cleaned dataset.
Revenue was recalculated from quantity multiplied by unit price.
