import click
import pandas as pd
import os
import logging
from rtgs.utils import setup_logging, create_output_dirs


@click.command()
@click.argument("file", type=click.Path(exists=True))
def clean(file):
    """Clean standardized dataset and save cleaned version."""
    setup_logging()

    dataset_name = os.path.splitext(os.path.basename(file))[0].replace("_standardized", "")
    create_output_dirs(dataset_name)

    try:
        logging.info(f"[Clean] Loading dataset: {file}")
        df = pd.read_csv(file)

        # Drop empty rows
        df = df.dropna(how="all")

        # Fill numeric NaN with mean
        num_cols = df.select_dtypes(include="number").columns
        for col in num_cols:
            if df[col].isna().any():
                df[col] = df[col].fillna(df[col].mean())

        out_path = os.path.join("data", "processed", f"{dataset_name}_cleaned.csv")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        df.to_csv(out_path, index=False)

        logging.info(f"[Clean] Completed for {dataset_name}, output={out_path}")
        click.echo(f"Cleaned dataset saved: {out_path}")

    except Exception as e:
        logging.error(f"[Clean] Failed for {dataset_name}: {e}")
        click.echo(f"Error during cleaning: {e}")
