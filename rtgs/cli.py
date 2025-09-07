import click
from rtgs.ingest import ingest
from rtgs.clean import clean
from rtgs.analyze import analyze


@click.group()
def app():
    """RTGS CLI for Telangana Open Data"""
    pass


# Register commands
app.add_command(ingest)
app.add_command(clean)
app.add_command(analyze)


if __name__ == "__main__":
    app()
