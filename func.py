def Sign(x: float) -> int:
    return x / abs(x) if x else 0


def RootCount(a: float, b: float, c: float):
    D = b**2 - 4*a*c
    if 0 > D:
        return "нету решений"

    D **= 0.5

    x1 = (-1*b + D) / (2*a)
    x2 = (-1 * b - D) / (2 * a)


def Calc(A: float, B: float, Op: int) -> float:
    if Op == 1:
        return A - B
    elif Op == 2:
        return A * B
    elif Op == 3:
        return A / B
    else:
        return A + B


def Even(K: int) -> bool:
    return K % 2 == 0


def DegToRad(D: float, pi: float = 3.14) -> float:
    return D * pi / 180


def RadToDeg(R: float, pi: float = 3.14) -> float:

    degrees = R * (180 / pi)
    return degrees


def Mean(X: float, Y: float) -> (float, float):
    arithmetic_mean = (X + Y) / 2
    geometric_mean = (X - Y) ** 0.5

    return arithmetic_mean, geometric_mean


def RectPS(x1: float, y1: float,
           x2: float, y2: float
           ) -> (float, float):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area


def GCD2(A: int, B: int) -> int:
    while B != 0:
        A, B = B, A % B
    return A


def Frac1(a: int, b: int
          ) -> (int, int):
    gcd = GCD2(a, b)
    p = a // gcd
    q = b // gcd
    return p, q


def LCM2(A: int, B: int) -> int:
    return A * (B // GCD2(A, B))


def GCD3(A: int, B: int, C: int) -> int:
    gcd_ab = GCD2(A, B)
    gcd_abc = GCD2(gcd_ab, C)
    return gcd_abc


def Leng(xA: float, yA: float,
         xB: float, yB: float):
    length = ((xA - xB)**2 + (yA - yB)**2)**0.5
    return length


def Perim(xA: float, yA: float,
          xB: float, yB: float,
          xC: float, yC: float):
    AB = Leng(xA, yA, xB, yB)
    BC = Leng(xB, yB, xC, yC)
    CA = Leng(xC, yC, xA, yA)
    return AB + BC + CA

# 1 2 7 9 17 18 24 26 46-49 56 57
# 58 59 60