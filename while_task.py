def a_b(func):
    def wrapper():
        a = int(input("a>"))
        b = int(input("b>"))
        print((a, b))

    return wrapper

def a_b(func):
    def wrapper():
        n = int(input("a>"))
        k = int(input("b>"))
        print(func(n, k))

    return wrapper


def g_p(func):
    def wrapper():
        p = float(input("p>"))
        print(func(p))

    return wrapper


def g_n(func):
    def wrapper():
        n = float(input("n>"))
        print(func(n))

    return wrapper


@a_b
def while2(a, b):
    count = 0

    while a >= b:
        count += 1
        a -= b

    return count


@a_b
def while3(n, k):
    q = 0
    r = n
    while r >= k:
        q += 1
        r -= n

    return f'Частное: {q},  Остаток:{r}'


@a_b
def while5(n):
    d = 0

    while n > 1:
        n = n // 2
        d += 1
    return d


@g_n
def while8(n):
    k = 0

    while not k**2 > n:
        k += 1

    return k-1


@g_n
def while12(n):
    k = 1
    s = k
    while not s > n:
        k += 1
        s += k

    return f"k={k-1}, s={s-k}"


@g_n
def while13(A):
    sum = 0
    K = 0

    while sum <= A:
        K += 1
        sum += 1 / K

    return f"{sum=}, {K=}"


@g_p
def while16(P):

    distance = 10  # initial distance
    total_dist = distance
    K = 1  # number of days

    while total_dist <= 200:
        K += 1
        distance *= (1 + P / 100)
        total_dist += distance

    return K, total_dist


@g_n
def while18(n):
    number = n
    sum_of_digits = 0
    l = 0
    while number > 0:
        digit = number % 10
        sum_of_digits += digit
        number //= 10
        l += 1

    return l, sum_of_digits


@g_n
def while21(n):
    number = n

    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            return True
        number //= 10

    return False


@g_n
def while25(n):
    a = 0
    b = 1

    while b <= n:
        a, b = b, a + b

    return b


@g_n
def while26(n):
    # Calculate the golden ratio
    phi = (1 + 5 ** 0.5) / 2

    # Calculate the previous Fibonacci number
    previous = round(n / phi)

    # Calculate the next Fibonacci number
    next_ = round(n * phi)

    return previous, next_


import math


@g_n
def find_ordinal_number(n):
    sqrt_five = math.sqrt(5)
    phi = (1 + sqrt_five) / 2

    ordinal_number = round(math.log(n * sqrt_five) / math.log(phi))
    return ordinal_number


# TODO: 2 3 5 8 12 13 16 18 21 25-27


if __name__ == "__main__":
    while21()