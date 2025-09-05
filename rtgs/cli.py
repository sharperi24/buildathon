import typer
from . import ingest, clean, analyze
from rtgs.logger import logger


app = typer.Typer()

@app.command()
def ingest_data(file: str):
    """Ingest raw dataset and standardize column names"""
    ingest.run(file)
    logger.info(f"Starting ingest for {file}")
    # do processing...
    logger.info(f"Finished ingest for {file}")

@app.command()
def clean_data(file: str):
    """Clean and transform dataset"""
    clean.run(file)
    logger.info(f"Starting cleaning for {file}")
    # do processing...
    logger.info(f"Finished cleaning for {file}")

@app.command()
def analyze_data(file: str):
    """Analyze dataset and extract insights"""
    analyze.run(file)
    logger.info(f"Starting analysis for {file}")
    # do processing...  
    logger.info(f"Finished analysis for {file}")

if __name__ == "__main__":
    app()
