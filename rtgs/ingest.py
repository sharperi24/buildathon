import click
import pandas as pd
import os
import logging
from rtgs.utils import setup_logging, create_output_dirs


@click.command()
@click.argument("file", type=click.Path(exists=True))
def ingest(file):
    """Ingest raw dataset and save standardized version."""
    setup_logging()

    dataset_name = os.path.splitext(os.path.basename(file))[0]
    create_output_dirs(dataset_name)

    try:
        df = pd.read_csv(file)
        logging.info(f"[Ingest] Started for {dataset_name}, shape={df.shape}")

        # Standardize column names
        df.columns = (
            df.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )

        out_path = os.path.join("data", "processed", f"{dataset_name}_standardized.csv")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        df.to_csv(out_path, index=False)

        logging.info(f"[Ingest] Completed for {dataset_name}, output={out_path}")
        click.echo(f"Standardized dataset saved: {out_path}")

    except Exception as e:
        logging.error(f"[Ingest] Failed for {dataset_name}: {e}")
        click.echo(f"Error during ingestion: {e}")
