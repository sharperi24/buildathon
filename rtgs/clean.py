import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def clean_dataset(file: str):
    logger.info(f"[Clean] Loading dataset: {file}")
    df = pd.read_csv(file)

    # 1. Standardize column names
    df.columns = (
        df.columns.str.strip()
                 .str.lower()
                 .str.replace(" ", "_")
                 .str.replace("-", "_")
    )

    # 2. Handle missing values
    missing_report = df.isna().sum().to_dict()
    logger.info(f"[Clean] Missing values per column: {missing_report}")

    # Drop rows where ALL values are NaN
    df = df.dropna(how="all")

    # Fill missing values
    num_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(include="object").columns

    for col in num_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].mean())

    for col in cat_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna("Unknown")

    # 3. Try to parse datetime-like columns
    for col in df.columns:
        if "date" in col or "time" in col:
            try:
                df[col] = pd.to_datetime(df[col] , format="%Y-%m-%d")
            except Exception:
                pass

    # 4. Save cleaned dataset
    out_path = "data/processed/cleaned.csv"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)

    logger.info(f"[Clean] Saved cleaned dataset to {out_path}")
    return df
