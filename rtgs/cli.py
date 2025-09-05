import typer
from . import ingest, clean, analyze

app = typer.Typer()

@app.command()
def ingest_data(file: str):
    """Ingest raw dataset and standardize column names"""
    ingest.run(file)

@app.command()
def clean_data(file: str):
    """Clean and transform dataset"""
    clean.run(file)

@app.command()
def analyze_data(file: str):
    """Analyze dataset and extract insights"""
    analyze.run(file)

if __name__ == "__main__":
    app()
