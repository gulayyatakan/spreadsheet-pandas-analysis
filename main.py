import pandas as pd
from pathlib import Path
import argparse

def load_data(path: Path) -> pd.DataFrame:
    """Load and clean the bestsellers dataset."""
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)
    df.rename(columns={"Name": "Title", "Year": "Publication_Year"}, inplace=True)
    df["Price"] = df["Price"].astype(float)
    return df

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate analysis reports for the Amazon Bestsellers dataset."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("bestsellers.csv"),
        help="Path to the input CSV file (default: bestsellers.csv)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs"),
        help="Directory to save the output reports (default: outputs/)",
    )
    return parser.parse_args()


def generate_reports(df: pd.DataFrame, out_dir: Path) -> None:
    """ Generate simple CSV reports in the given output directory. """
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1) Author counts
    author_counts = df["Author"].value_counts()
    author_counts.to_csv(out_dir / "author_counts.csv")

    # 2) Average rating by genre
    avg_rating_by_genre = (
        df.groupby("Genre")["User Rating"]
        .mean()
        .sort_values(ascending=False)
    )
    avg_rating_by_genre.to_csv(out_dir / "avg_rating_by_genre.csv")

    # 3) Average rating by year
    avg_rating_by_year = (
        df.groupby("Publication_Year")["User Rating"]
        .mean()
        .round(3)
        .sort_index()
    )
    avg_rating_by_year.to_csv(out_dir / "avg_rating_by_year.csv")


def main() -> None:
    args = parse_args()
    df = load_data(args.input)

    print("\n")
    print("=== Amazon Bestsellers summary ====")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print()
    print("Top 5 rows")
    print(df.head())

    generate_reports(df, args.output)
    print(f"\nReports written to: {args.output.resolve()}")

if __name__ == "__main__":
    main()