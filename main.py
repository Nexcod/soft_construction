import typer

from myparser import get_data
from solution import method_two
from tabulate import tabulate


app = typer.Typer()



@app.command()
def method_one():
    typer.echo(tabulate(get_data()))


@app.command()
def method_twoo():
    method_two()


@app.command()
def method_three():
    pass


@app.command()
def method_four():
    pass


if __name__ == '__main__':
    app()
