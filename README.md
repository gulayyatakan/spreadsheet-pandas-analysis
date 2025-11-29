# Amazon Bestsellers Explorer

Small practice project using Python, pandas, and Streamlit to explore an Amazon bestsellers dataset from a CSV file.

## What it does

- Loads and cleans `bestsellers.csv` (removes duplicates, renames columns, fixes types)
- Lets you filter books by genre in a Streamlit sidebar
- Shows a preview of the filtered data
- Displays the top N books by number of reviews
- Visualizes rating distribution and average rating per publication year

## How to run

```bash
# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```
# run the Streamlit app
streamlit run app.py