import math

a = [9, 12, 11, 4, 7, 2, 5, 8, 5, 7, 1, 6, 1, 9, 4, 1, 3, 3, 6, 1, 11, 33, 7, 91, 2, 1]

lenghA = len(a)

HIGH = 100000

STEP = 0.0001


def left(b):
    result = 0
    j = 1
    for i in range(lenghA):
        result += (1 / (b - j + 1))
        j += 1
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
        if (r > r1):
            break
        d = d + STEP

    print(d)
