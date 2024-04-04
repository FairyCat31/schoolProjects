def a_b(func):
    def wrapper():
        a = int(input("a>"))
        b = int(input("b>"))
        func(a, b)

    return wrapper


def g_p(func):
    def wrapper():
        p = float(input("p>"))
        func(p)

    return wrapper


def g_n(func):
    def wrapper():
        n = float(input("n>"))
        func(n)

    return wrapper


# @a_b
# def while1(a, b):
#     c = 0
#     for _ in range(1, a, b):
#         c += 1
#
#     c = a-(c*b if a > b*c else (c-1)*b)
#
#     print(f"{c=}")
#
# @a_b
# def while2(a, b):
#     c = 0
#     for _ in range(1, a, b):
#         c += 1
#
#     c = c if a > b*c else c-1
#
#     print(f"{c=}")
#
# @a_b
# def while3(a, b):
#     c = 0
#     for _ in range(1, a, b):
#         c += 1
#
#     c = a - (c * b if a > b * c else (c - 1) * b)
#     a -= c
#
#     print(f"Частное: {a}\nОстаток {c}")

def while11():

    n = int(input("dd"))

    k, s = 0, 0

    while s < n:
        k += 1
        s += k


@g_p
def while15(p):
    s = 1000
    m = 0
    while s < 1100:
        s += s*p/100
        m += 1
        print(m, s)

    print(m)


@g_n
def while18(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10

    print(s)


# TODO: 1-12 14 15 18 19 21 28 30 33 36 40
if __name__ == "__main__":
    while18()