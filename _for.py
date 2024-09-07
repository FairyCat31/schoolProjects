

def for1():
    k = int(input("Введите K>"))
    n = int(input("Введите N>"))

    for i in range(n):
        print(f"{i+1}) {k}")


def for3():
    a = int(input("Введите a>"))
    b = int(input("Введите b>"))

    for i in range(b, a-1, -1):
        print(i)

    print(f'n={b-a}')


def for2():
    a = int(input("Введите a>"))
    b = int(input("Введите b>"))


    for i in range(a, b+1):
        print(i)


    print(f'n={b-a}')


def for4():
    p = float(input("Введите price>"))
    for i in range(1, 11):
        print(f"Цена: {i*p}руб за {i} кг")


def for5():
    p = float(input("Введите price>"))
    for i in range(1, 11):
        print(f"Цена: {(i*0.1)*p}руб за {i*0.1} кг")


def for6():
    p = float(input("Введите price>"))
    for i in range(1, 6):
        print(f"Цена: {(1+i*0.2)*p}руб за {1+i*0.2} кг")


def for7():
    a = int(input("введите а> "))
    b = int(input("введите b> "))
    c = 0
    for i in range(a, b+1):
        c += i
    print(f"Сумма всех ч равна {c}")


def for8():
    a = int(input("введите а> "))
    b = int(input("введите b> "))
    c = 1
    for i in range(a, b+1):
        c *= i
    print(f"произведение всех ч равно {c}")


def for9():
    a = int(input("введите а> "))
    b = int(input("введите b> "))
    c = 0
    for i in range(a, b+1):
        c += i**2
    print(f"Сумма квадратов всех ч равна {c}")


def for10():
    n = int(input("введите n> "))
    c = 0
    for i in range(1, n+1):
        c += 1/i
    print(f"Сумма всех обычных дробей равна {c}")


def for12():
    n = int(input("введите n> "))
    c = 1
    for i in range(1, n+1):
        c *= (1 + i/10**len(str(i)))
    print(f"Произведение всех десятичных дробей равно {c}")


def for14():
    n = int(input("введите n> "))
    n2 = 0
    for i in range(1, 2*n, 2):
        n2 += i
    print(f"Число {n} во 2-ой степени = {n2}")


def for15():
    a = int(input("введите a> "))
    n = int(input("введите n> "))
    a2 = a
    for i in range(1, n):
        a2 *= a
    print(f"Число {a} во {n}-ой степени = {a2}")


def main():
    for15()

# TODO: 1-12 14 15 18 19 21-28 30 33 36 40

if __name__ == "__main__":
    main()