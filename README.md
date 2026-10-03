<div align="center">

# 🛒 Retail Sales Analysis

**End-to-end retail sales analysis — SQL queries, Python processing, and an interactive Streamlit dashboard.**

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

</div>

Analyze retail sales data to identify top products, cities, and trends — from raw SQL queries through Python data processing to a live interactive dashboard.

## ✨ Features

- **SQL-based analysis** — schema, inserts, and queries in `queries.sql`
- **Python data processing** — cleaning and transformation in `cleaning_code.py`
- **Excel insights** — spreadsheet-ready outputs
- **Interactive Streamlit dashboard** — filter by city, view charts live
- **Real dataset** — `sales_data.csv`

## 📊 Key Insights

- 💻 **Laptop** generates the highest revenue
- 🏙️ **Mumbai** leads in sales
- 🧾 **Electronics** dominate the market

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10 |
| Data | Pandas · Matplotlib |
| Dashboard | Streamlit |
| Queries | SQL |

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python -m streamlit run main.py
```

The dashboard opens at <http://localhost:8501>.

## 📁 Project Structure

```
Retail-Sales-Analysis/
├── main.py            # Streamlit dashboard
├── cleaning_code.py   # Data cleaning & processing
├── queries.sql        # SQL schema + analysis queries
├── sales_data.csv     # Retail sales dataset
└── requirements.txt
```

## 📄 License

[MIT](LICENSE) © Priyanshu Rout