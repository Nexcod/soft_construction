import typer
from solution import method_two as petr_solution
from tabulate import tabulate
from parser import get_data
from stas_solution import *
from findRoot import *

app = typer.Typer()


@app.command()
def method_one():
    typer.echo(tabulate(get_data()))


@app.command()
def method_two():
    petr_solution()


@app.command()
def method_three():
	findRoot()

	
	
	
@app.command()
def method_four():
    pass


if __name__ == '__main__':
    app()
