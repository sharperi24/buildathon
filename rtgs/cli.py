import click
from rtgs.ingest import ingest_dataset
from rtgs.clean import clean_dataset
from rtgs.analyze import analyze_dataset
import os

@click.group()
def app():
    """RTGS CLI for Telangana Open Data"""
    pass


# ------------------------
# Ingest Command
# ------------------------
@app.command()
@click.argument("file")
def ingest(file):
    """Load raw dataset and standardize column names."""
    df = ingest_dataset(file)
    click.echo(f" Ingested {len(df)} rows from {file}")


# ------------------------
# Clean Command
# ------------------------
@app.command()
@click.argument("file")
def clean(file):
    """Clean raw dataset and save analysis-ready version."""
    df = clean_dataset(file)
    click.echo(f" Cleaned dataset saved with {len(df)} rows")


# ------------------------
# Analyze Command
# ------------------------
@app.command()
@click.argument("file")
def analyze(file):
    """Analyze any cleaned dataset (dataset-agnostic)."""
    results = analyze_dataset(file)

    click.echo("\n=== Dataset Overview ===")
    click.echo(f"Rows: {results['rows']}, Columns: {results['columns']}")
    click.echo("\nMissing values per column:")
    for col, missing in results["missing"].items():
        click.echo(f" {col}: {missing}")

    click.echo("\nReports saved to: out/reports/")
    click.echo("Plots saved to: out/plots/")

    # Optionally, list top/bottom 5 CSVs generated
    top_bottom_files = [f for f in os.listdir("out/reports") if "top5" in f or "bottom5" in f]
    if top_bottom_files:
        click.echo("\nTop/Bottom 5 highlights:")
        for f in top_bottom_files:
            click.echo(f" - {f}")


# ------------------------
# Entrypoint
# ------------------------
if __name__ == "__main__":
    app()
