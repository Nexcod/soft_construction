import typer

from myparser import get_data
from solution import method_two as mt
from solution import find_k as K
from solution import av_time as av
from solution import time_to_test_end as time
from tabulate import tabulate

app = typer.Typer()


@app.command()
def method_one():
    typer.echo(tabulate(get_data()))


@app.command()
def method_two(args):
    print("Максимальное правдоподобие для общего числа ошибок:", mt())
    print("Коэффициент пропорциональности K: ", K())
    print("Среднее время до появления следующей ошибки:", av())
    print("Вреямя до окончания тестирования:", time())


method_two(get_data())


@app.command()
def method_three():
    pass


@app.command()
def method_four():
    pass


if __name__ == '__main__':
    app()
