import math

from myparser import get_data

a = ([int(x[1]) for x in get_data()])

lenghA = len(a)

HIGH = 100000

STEP = 0.0001


def left(b):
    result = 0
    j = 1
    for i in range(lenghA):
        result += (1 / (b - j + 1))
        j = j + 1

    return result


# Сумма интервалов между ошибками.

def getSum():
    result = 0
    for i in range(lenghA):
        result += a[i]

    return result


# Сумма произведений интервалов между ошибками на их порядковый номер.

def getSumI():
    result = 0
    j = 1
    for i in range(lenghA):
        result += j * a[i]
        j += 1

    return result


def right(b):

    return (lenghA * getSum()) / ((b + 1) * getSum() - getSumI())


def method_two():
    d = lenghA
    r = math.inf
    for i in range(HIGH):
        r1 = r
        r = abs(left(d) - right(d))
        # Если текущая разница превысит предыдущую разницу, выходим
        if r > r1:
            break
        d = d + STEP

    return d


def find_k():
    return lenghA / ((method_two() + 1) * getSum() - getSumI())


def av_time():
    return 1 / (find_k() * (method_two() - lenghA))


def time_to_test_end():
    result = 0

    for i in range(1, int(method_two()) - lenghA):
        result += (1 / i)

    return (1 / find_k()) * result
