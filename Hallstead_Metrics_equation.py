l = 1.53
B = [2, 5, 4, 0]
V = [5, 7, 9, 11]



def R(t):
    if t == 0:
        return 1000

    sumV = 0
    for j in range (0,4):
        sumV += V[j]


    sumB = 0
    for k in (1, t):
        sumB += B[k-1]/c(l, R(k-1))

    diff = sumV - sumB
    res = (1+diff/1000)*R(t-1)
    return res

def c(l, r):
    return 1/(l+r)
    #return 1/l*r
    #return 1/l + 1/r

def result():
    r = R(4)
    print("Текущий рейтинг программиста: ", r)
    b = c(l, r)*15
    print("Потенциальное количество ошибок в 5-й программе: ", b)