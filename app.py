import streamlit as st
import pandas as pd

# --- Title & intro ---
st.title("Amazon Bestsellers - Explorer")
st.write(
    "Willkommen zum Amazon Bestseller Explorer! "
    "Hier können Sie die beliebtesten Bücher analysieren."
)

# --- Data loading & cleaning ---
@st.cache_data
def load_data(file) -> pd.DataFrame:
    df = pd.read_csv(file)
    df.drop_duplicates(inplace=True)
    df.rename(columns={"Name": "Title", "Year": "Publication_Year"}, inplace=True)
    df["Price"] = df["Price"].astype(float)
    return df


#--- Sidebar: file upload ---
st.sidebar.header("Upload your CSV data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is None:
    st.warning("Please upload a CSV file to start.")
    st.stop()

df = load_data(uploaded_file)

# --- Sidebar filters ---
st.sidebar.header("Filters")

all_genres = ["All"] + sorted(df["Genre"].unique().tolist())
selected_genre = st.sidebar.selectbox("Genre", all_genres)

if selected_genre != "All":
    filtered_df = df[df["Genre"] == selected_genre]
else:
    filtered_df = df

# --- Dataset preview ---
st.subheader("Dataset Preview")
st.write(filtered_df.head())
st.write(f"Shape: {filtered_df.shape[0]} rows and {filtered_df.shape[1]} columns")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download data as CSV",
    data=csv_data,
    file_name="bestsellers_filtered.csv",
    mime="text/csv",
)


# --- Top N books ---
st.subheader("Top N books by number of reviews")

top_n = st.slider(
    "Number of books to show",
    min_value=5,
    max_value=30,
    value=10,
)

top_reviewed = (
    filtered_df
    .sort_values(by="Reviews", ascending=False)
    .head(top_n)
)

st.write(
    top_reviewed[
        ["Title", "Author", "User Rating", "Reviews", "Price", "Publication_Year"]
    ]
)

# --- Rating distribution ---
st.subheader("Rating distribution")

rating_counts = (
    filtered_df["User Rating"]
    .value_counts()
    .sort_index()  # Sort by rating value
)

st.bar_chart(rating_counts)

# --- Avg rating by year ---
st.subheader("Average rating by publication year")

avg_rating_by_year = (
    filtered_df
    .groupby("Publication_Year")["User Rating"]
    .mean()
    .sort_index()
    .reset_index()
)

st.line_chart(
    data=avg_rating_by_year,
    x="Publication_Year",
    y="User Rating",
)