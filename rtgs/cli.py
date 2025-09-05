import click
from rtgs.ingest import ingest_dataset
from rtgs.clean import clean_dataset
from rtgs.analyze import analyze_rainfall


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
@click.option("--district", default=None, help="Filter by district")
def analyze(file, district):
    """Analyze cleaned rainfall dataset."""
    results = analyze_rainfall(file, district)

    click.echo("\n=== Average Rainfall by District ===")
    click.echo(results["avg_table"])

    click.echo(f"\n Wettest District: {results['wettest'][0]} ({results['wettest'][1]} mm avg)")
    click.echo(f" Driest District: {results['driest'][0]} ({results['driest'][1]} mm avg)")
    click.echo(f" Heavy Rainfall Days (>20mm): {results['heavy_days']}")


# ------------------------
# Entrypoint
# ------------------------
if __name__ == "__main__":
    app()
