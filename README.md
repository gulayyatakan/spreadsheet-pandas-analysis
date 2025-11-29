# Spreadsheet Analysis with Pandas

This project explores an Amazon bestsellers dataset using Python and pandas.  
It includes both a simple data analysis script and an interactive Streamlit app.

## Features

- Load and clean the `bestsellers.csv` dataset (remove duplicates, rename columns, convert types)
- Filter books by genre
- View top N books by number of reviews
- Inspect rating distribution
- See average rating per publication year

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt