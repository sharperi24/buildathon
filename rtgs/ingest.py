import pandas as pd

def run(file: str):
    print(f"[Ingest] Loading dataset: {file}")
    df = pd.read_csv(file)
    print(f"[Ingest] Shape: {df.shape}")
    # Save standardized output
    out_path = "data/processed/standardized.csv"
    df.to_csv(out_path, index=False)
    print(f"[Ingest] Saved standardized dataset to {out_path}")
