import pandas as pd
import os

def run(file: str):
    print(f"[Clean] Loading dataset: {file}")
    df = pd.read_csv(file)

    # 1. Standardize column names
    df.columns = (
        df.columns.str.strip()       # remove spaces at ends
                 .str.lower()        # lowercase
                 .str.replace(" ", "_")  # spaces → underscore
                 .str.replace("-", "_")  # dashes → underscore
    )

    # 2. Handle missing values
    missing_report = df.isna().sum()
    print("[Clean] Missing values:\n", missing_report)

    # Example strategy: drop rows where ALL columns are NaN
    df = df.dropna(how="all")

    # Example strategy: fill numeric NaN with column mean
    num_cols = df.select_dtypes(include="number").columns
    for col in num_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].mean())

    # 3. Convert datatypes (example: ensure "year" is int)
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

    # 4. Save cleaned dataset
    out_path = "data/processed/cleaned.csv"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)

    print(f"[Clean] Saved cleaned dataset to {out_path}")
    return df
