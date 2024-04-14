def Sign(x: float) -> int:
    return x / abs(x) if x else 0


def RootCount(a: float, b: float, c: float):
    D = b**2 - 4*a*c
    if 0 > D:
        return "нету решений"

    D **= 0.5

    x1 = (-1*b + D) / (2*a)
    x2 = (-1 * b - D) / (2 * a)