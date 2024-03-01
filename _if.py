"""
4 5 9 11 13 14 16 17 20 21 22 23 26 28
"""


def if1():
    a = int(input("Введите число> "))
    print(a-8 if a > 0 else a)


def if2():
    a = int(input("Введите число> "))
    print(a-8 if a > 0 else a+6)


def if3():
    a = int(input("Введите число> "))
    if a > 0:
        a -= 8
    elif a < 0:
        a += 6
    else:
        a = 10
    print(a)


def if4():
    nums = input("Введите числа(например> 20 -4 7) > ").split(" ")
    a = 0
    for num in nums:
        if int(num) > 0:
            a += 1

    print(f"Всего положительных чисел: {a}")


def if5():
    nums = input("Введите числа(например> 20 -4 7) > ").split(" ")
    a = 0
    b = 0
    for num in nums:
        if int(num) > 0:
            a += 1
        if int(num) < 0:
            b += 1
    print(f"Всего положительных чисел: {a}\nВсего отрицательных чисел: {b}")


def if9():
    a = float(input("Введите число a> "))
    b = float(input("Введите число b> "))
    if a > b:
        a, b = b, a
    print(f"{a=}, {b=}")


def if11():
    a = int(input("Введите число a> "))
    b = int(input("Введите число b> "))
    if a == b:
        a = b = 0
        print(f"{a=}, {b=}")
        return 0

    a = a if a > b else b
    b = a
    print(f"{a=}, {b=}")


def if13():
    a = int(input("Введите число a> "))
    b = int(input("Введите число b> "))
    c = int(input("Введите число c> "))

    if a > b > c or c > b > a:
        print(f"{b=}")
    elif a > c > b or b > c > a:
        print(f"{c=}")
    else:
        print(f"{a=}")


def if14():
    a = int(input("Введите число a> "))
    b = int(input("Введите число b> "))
    c = int(input("Введите число c> "))
    if a > b and a > c:
        print(f"большее {a=}")
    elif b > a and b > c:
        print(f"большее {b=}")
    else:
        print(f"большее {c=}")

    if a < b and a < c:
        print(f"наименьшее {a=}")
    elif b < a and b < c:
        print(f"наименьшее {b=}")
    else:
        print(f"наименьшее {c=}")


def if16():
    a = float(input("Введите число a> "))
    b = float(input("Введите число b> "))
    c = float(input("Введите число c> "))

    if a > b > c:
        a *= 2
        b *= 2
        c *= 2
    else:
        a *= -1
        b *= -1
        c *= -1

    print(f"{a=}, {b=}, {c=}")


def if17():
    a = float(input("Введите число a> "))
    b = float(input("Введите число b> "))
    c = float(input("Введите число c> "))

    if a > b > c or a < b < c:
        a *= 2
        b *= 2
        c *= 2
    else:
        a *= -1
        b *= -1
        c *= -1

    print(f"{a=}, {b=}, {c=}")


def if20():
    a = int(input("Введите число a> "))
    b = int(input("Введите число b> "))
    c = int(input("Введите число c> "))
    ac = abs(a - c)
    ab = abs(a - b)
    print(f"{ab=}" if ab < ac else f"{ac=}")


def if21():
    x0 = int(input("Введите число x> "))
    y0 = int(input("Введите число y> "))

    if not x0 and not y0:
        print(0)
        return 0
    if not x0:
        print(1)
        return 1
    elif not y0:
        print(2)
        return 2
    else:
        print(3)
        return 3


def if22():
    x0 = int(input("Введите число x> "))
    y0 = int(input("Введите число y> "))

    if x0 > 0:
        print(2 if y0 > 0 else 4)
    else:
        print(1 if y0 > 0 else 3)


def if23():
    x1 = input("Введите коорды x1 точки> ")
    y1 = input("Введите коорды y1 точки> ")
    x2 = input("Введите коорды x2 точки> ")
    y2 = input("Введите коорды y2 точки> ")
    x3 = input("Введите коорды x3 точки> ")
    y3 = input("Введите коорды y3 точки> ")

    x4 = x3 if x1 == x2 else (x2 if x1 == x3 else x1)
    y4 = y3 if y1 == y2 else (y2 if y1 == y3 else y1)

    print(f"{x4=}, {y4=}")


def if26():
    x = float(input("Введите аргумент x>"))
    if x <= 0:
        print(-x)
    elif x >= 2:
        print(4)
    else:
        print(x**2)


def if28():
    x = int(input("Введите год> "))
    if x % 4:
        print("Не високосный")
        return 0
    if not x % 100:
        if x % 400:
            print("Не високосный")
            return 0
    print("високосный")


def main():
    if28()


if __name__ == "__main__":
    main()