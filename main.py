import typer
from solution import method_two as petr_solution

from solution import method_two as mt
from solution import find_k as K
from solution import av_time as av
from solution import time_to_test_end as time
from tabulate import tabulate

from myparser import get_data
from stas_solution import *

app = typer.Typer()


@app.command()
def method_one():
    typer.echo(tabulate(get_data()))


@app.command()
def method_two():
    print("Максимальное правдоподобие для общего числа ошибок:", mt())
    print("Коэффициент пропорциональности K: ", K())
    print("Среднее время до появления следующей ошибки:", av())
    print("Вреямя до окончания тестирования:", time())
    petr_solution()


@app.command()
def method_three():
    s = findAppoximateRootValue()
    print(s)
    checkRoot()


@app.command()
def method_four():
    pass


if __name__ == '__main__':
    app()
