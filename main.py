import typer
from tabulate import tabulate

from parser import get_data

app = typer.Typer()


@app.command()
def method_one():
    typer.echo(tabulate(get_data()))


@app.command()
def method_two():
    pass


@app.command()
def method_three():
    pass


@app.command()
def method_four():
    pass


if __name__ == '__main__':
    app()
