import math

def Hallstead1and2():

    n = 6060
    V = (n+2)*math.log((n+2),2)

    print("ЗАДАНИЕ 1")
    print("Потенциальный объем программы:", V)

    B = (V*V)/(3000*1.53)

    print("Потенциальное число ошибок: ", B)

    print("ЗАДАНИЕ 2")

    K = (n/8)+(n/(8**2))

    print("Число модулей программного средства:", K)

    N = (220*K) + (K*math.log(K, 2))

    print("Расчетная длина программы:", N)

    Vol = K * 220 * math.log(48, 2)

    print("Расчетный объем ПО:", Vol)

    P = (3*N)/8

    print("Расчетное количество команд ассемблера:", P)

    T = (3*N)/(8*4*28)

    print("Календарное время программирования:", T, "дней")


    Pot_kol = Vol/3000

    print("Потенциальное количество ошибок:", Pot_kol)

    t = T/(2*math.log(B))

    print("Начальная надежность ПО:", t)

    print("ЗАДАНИЕ 3")