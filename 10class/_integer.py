def integer1():
    l = int(input("l в см> "))
    print(f"{l // 100} м")


def integer3():
    s = int(input("s в байтах> "))
    print(f"{s // 1024} килобайт")


def integer4():
    a, b = int(input("а длина> ")), int(input("б длина> "))
    print(f"{a // b} кол во отрезков б в отрезке а")


def integer7():
    ln = input("Введите число> ")
    x = int(ln[0])
    y = int(ln[1])
    print(f"Сумма {x + y}, а произведение {x * y}")


def integer12():
    print(input("Введите число> ")[::-1])


def integer14():
    n = input("Число > ")
    print(n[-1:] + n[:-1])


def integer18():
    n = int(input("Введите число > "))
    print(f"разряд тысяч {(n // 1000) % 10}")


def integer20():
    print(f"Прошло часов {int(input('Введите кол во секунд> ')) // 3600}")


def integer23():
    print(f"прошло минут c последнего часа {(int(input('Введите кол во секунд> ')) % 3600) // 60}")


def integer24():
    days = ["вс", "пн", "вт", "ср", "чт", "пт", "сб"]
    print(f" Сегодня {days[(int(input('День 1-365> '))) % 7]}")


def integer28():
    days = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
    k, n = int(input("День в году 1-365> ")), int(input("День в недели 1-7> "))
    l = (k+n-1) % 7
    print(days[l-1], l if l else 7)


def integer29():
    a, b, c = int(input("a=")), int(input("b=")), int(input("c="))
    S = a*b
    s = (a//c)*(b//c)
    print(f"Квадратов {s} и площадь не занята {S-(s*c**2)}")


def integer30():
    s = int(input("Введите год > "))
    print(f"Это {int(str(s-1)[:-2])+1} век")


def main():
    integer29()


if __name__ == "__main__":
    main()