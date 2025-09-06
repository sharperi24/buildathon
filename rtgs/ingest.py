import pandas as pd
from rtgs.logger import logger

def ingest_dataset(file: str, out_file: str = "data/processed/standardized.csv"):
    df = pd.read_csv(file)

    # Example standardization: lowercase column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    df.to_csv(out_file, index=False)
    logger.info(f"Ingested {file} -> standardized {df.shape[0]} rows, {df.shape[1]} columns -> {out_file}")
    return out_file
