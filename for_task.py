def for1():
    n = int(input("Введите n> "))
    k = int(input("Введите k> "))
    for _ in range(n): print(k)


def for2():
    a = int(input("Введите a> "))
    b = int(input("Введите b> "))
    n = 0
    for v in range(a, b+1):
        n += 1
        print(f"{n}) {v}")
    print(f"Всего чисел {n}")


def for3():
    a = int(input("Введите a> "))
    b = int(input("Введите b> "))
    n = 0
    for v in range(a-1, b, -1):
        n += 1
        print(f"{n}) {v}")
    print(f"Всего чисел {n}")


def for4():
    p = float(input("Цена за 1кг конфет> "))
    for i in range(1, 11):
        print(f"Цена за {i} кг = {p*i}")


def for5():
    p = float(input("Цена за 1кг конфет> "))
    for i in range(1, 11):
        print(f"Цена за {i / 10} кг = {p * (i / 10)}")


def for6():
    p = float(input("Цена за 1кг конфет> "))
    for i in range(1, 6):
        k = 1 + 0.2 * i
        print(f"Цена за {k} кг = {p * k}")


def for7():
    a = int(input("Введите a> "))
    b = int(input("Введите b> "))
    n = 0
    for v in range(a, b+1):
        n += v
    print(f"Сумма всех чисел между {a} и {b} = {n}")


def for8():
    a = int(input("Введите a> "))
    b = int(input("Введите b> "))
    n = 1
    for v in range(a, b+1):
        n *= v
    print(f"Произведение всех чисел между {a} и {b} = {n}")


def for9():
    a = int(input("Введите a> "))
    b = int(input("Введите b> "))
    n = 0
    for v in range(a, b+1):
        n += v**2
    print(f"Сумма квадратов всех чисел между {a} и {b} = {n}")


def for10():
    n = int(input("Введите n> "))
    s = 0
    for v in range(1, n+1):
        s += 1/v

    print(f"Сумма всех дробей между 1 и 1\{n} = {s}")


def for11():
    n = int(input("Введите n> "))
    s = 0
    for v in range(n+1):
        s += (n+v)**2
    print(f"Сумма всех квадратов сумм между 1 и {n} = {s}")


def for12():
    n = int(input("Введите n> "))
    s = 1
    for v in range(1, (n-1)*10+1):
        s *= v/10 + 1
        print(v/10 + 1)
    print(f"Произведение всех дробей между 1 и {n} = {s}")


def for14():
    n = int(input("Введите n> "))
    s = 0
    for v in range(1, 2*n, 2):
        s += v

    print(f"Квадрат числа {n} = {s}")


def for15():
    a = float(input("Введите a> "))
    n = int(input("Введите n> "))
    s = 1
    for _ in range(n):
        s *= a

    print(f"{a} в степени {n} = {s}")


def for18():
    a = float(input("Введите a> "))
    n = int(input("Введите n> "))
    s = 0
    for i in range(n+1):
        s += ((-1)**i)*(a**i)

    print(f"Значения выражения = {s}")


def for19():
    n = int(input("Введите n> "))
    s = 1
    t = 0
    for i in range(1, n+1):
        t = s * i
        s = t

    print(f"{n}! = {t}")


def for21():
    N = int(input("Введите n> "))
    f = 1
    s = 1
    for i in range(1, N+1):
        f *= i
        s += 1.0 / f
    print(f"Значение выражение = {s}")


def for22():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    f = 1
    s = 1
    t = 1
    for i in range(1, n + 1):
        f *= i
        t *= x
        t /= i
        s += t
    print(f"Значение выражение = {s}")


def for23():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    r = 0
    f = 1
    for i in range(1, 2*n+2, 2):
        r += ((-1)*(i//2)) * (x*i) / f
        f *= (i+1) * (i+2)
    print(f"Значение выражение = {r}")


def for24():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    r = 1
    f = 1
    for i in range(1, 2*n+1, 2):
        r += ((-1)*(i//2)) * (x*i) / f
        f *= (i+1) * (i+2)
    print(f"Значение выражение = {r}")


def for25():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    r = 0
    for i in range(1, n+1):
        r += ((-1)*(i-1)) * (x*i) / i

    print(f"Значение выражение = {r}")


def for26():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    r = 0
    for i in range(1, n+1):
        r += ((-1)**(i+1)) * (x**(2*i-1)) / (2*i-1)
    return r
    print(f"Значение выражение = {r}")


def for27():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    r = x
    numerator = x
    for i in range(1, n+1):
        numerator *= ((2*i-1)*(2*i-1))
        r += (numerator / ((2*i)*(2*i+1)))
    print(f"Значение выражение = {r}")


def for28():
    x = float(input("Введите x> "))
    n = int(input("Введите n> "))
    r = 1
    t = 1
    f = 1
    for i in range(1, n+1):
        t *= x
        f *= 2*i * (2*i - 1)
        r += ((-1)**(i-1)) * (t / f)
    print(f"Значение выражение = {r}")


def for30():
    from math import sin

    A = float(input("Введите a> "))
    B = int(input("Введите b> "))
    N = int(input("Введите n> "))

    H = (B - A) / N
    values = [A + i * H for i in range(N + 1)]
    results = [1 - sin(x) for x in values]
    print(H, results)


def for33():
    N = int(input("Введите n> "))
    fib = [1, 1]
    for i in range(2, N):
        fib.append(fib[i - 2] + fib[i - 1])
    print(fib[:N])


def for36():
    K = int(input("Введите k> "))
    N = int(input("Введите n> "))
    r = 0.0
    for i in range(1, N + 1):
        r += i ** K
    print(f"Значение выражение = {r}")


def for40():
    A = int(input("Введите a> "))
    B = int(input("Введите b> "))
    for i in range(A, B + 1):
        print((str(i) + ' ') * (i - A + 1))

"""
18
19
21-28
30
33
36
40
"""
if __name__ == "__main__":
    pass