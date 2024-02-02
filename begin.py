
def begin3():
    a, b = int(input("Enter a's value> ")), int(input("Enter b's value> "))
    print(f"\nP={(a + b) * 2}\nS={a * b}")


def begin7():
    R = int(input("Введите 1 катет> "))
    Pi = 3.14
    print(f"")


def begin12():
    a, b = int(input("Введите 1 катет> ")), int(input("Введите 2 катет> "))
    c = (a**2 + b**2)**0.5
    print(f"\n{c=}\nP={a+b+c}")


def begin16():
    x1, x2 = int(input("Введите 1 кор> ")), int(input("Введите 2 кор> "))
    print(f"Разница={abs(x1-x2)}")


def begin19():
    x1, y1 = int(input("Введите x1 кор> ")), int(input("Введите y1 кор> "))
    x2, y2 = int(input("Введите x2 кор> ")), int(input("Введите y2 кор> "))

    a, b  = abs(x1-x2), abs(y1-y2)

    S = a*b
    P = (a+b)*2
    print(S, P)

def begin22():
    a, b = 4, 5
    a += b
    b -= a
    a -= b

    #or
    a, b = b, a

    print(a, b)


def begin25():
    x = int(input("Enter x>"))
    y = 3*x**6 - 6*x**2 - 7
    print(f"y={y}")


def begin29():
    a = int(input("Введите угол>"))
    print(a/180)


def begin31():
    F = float(input("F>"))
    print("C=", (F-32)*5/9)


def begin33():
    x, a = float(input("Введите массу> ")), float(input("Введите цену за эту массу> "))
    print(f"{x/a} кг/руб")


def begin34():
    x, a = float(input("Введите массу(шок конф)> ")), float(input("Введите цену за эту массу(шок конф)> "))
    y, b = float(input("Введите массу(ириски)> ")), float(input("Введите цену за эту массу(ириски)> "))
    print(f"{x / a} кг/руб")
    print(f"{y / b} кг/руб")
    print(f"в {(x/a)/(y/b)} шок конф больше стоят чем ириски")


def begin35():
    V = float(input("Скорость лодки км/ч> "))
    U = float(input("Скорость течения реки км/ч> "))
    T = float(input("Время пути ч> "))
    print(f"Растояние = {(V-U)*T}")


def begin40():
    a1, b1, c1 = float(input("A1 = ")), float(input("B1 = ")), float(input("C1 = "))
    a2, b2, c2 = float(input("A2 = ")), float(input("B2 = ")), float(input("C2 = "))
    D = a1 * b2 - a2 * b1
    x = (c1 * b2 - c2 * b1) / D
    y = (a1 * c2 - a2 * c1) / D

    print(f"x={x} и y={y}")


def main():
    begin34()


if __name__ == "__main__":
    main()