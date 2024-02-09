

def bool3():
    print("Четное?", int(input("Введите число> "))%2 == 0)


def bool4():
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))

    print("Справедливо А>2 |", A>2)
    print("Справедливо B<=3 |", B<=3)


def bool5():
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))

    print("Справедливо А>=0 |", A>=0)
    print("Справедливо B<-2 |", B<-2)


def bool6():
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))
    C = int(input("Введите C> "))

    print("Справедливо A<B<C |", A<B<C)


def bool7():
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))
    C = int(input("Введите C> "))

    print("Справедливо что В между А и С |", (A<B<C)or(C>B>A))


def bool11():
    """
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))

    for i in range(1, A if A>B else B):
        if A%2:
            continue
        else:
            if B%2:
                print("не общая четность")
                return 0

    print("общая четность")
    return 1 """
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))

    print("Одинаковая ли четность?", (A%2)==(B%2))


def bool17():
    A = input("Введите число> ")
    if len(A) != 3:
        print("Число не трёхзначное")
        return -2
    if int(A)%2:
        print("Число не четное")
        return -1
    else:
        print("Число трёхзначное и четное")
        return 0


def bool18():
    A = int(input("Введите A> "))
    B = int(input("Введите B> "))
    C = int(input("Введите C> "))

    print("Есть ли совпадения? |", (A==B)or(A==C)or(B==C))


def bool20():
    A = input("Введите число> ")
    print("Есть ли совпадения по числам? |", (A[0]==A[1])or(A[0]==A[2])or(A[1]==A[2]))


def bool22():
    A = input("Введите число> ")
    print("Есть ли убыв. или возраст. последовательность? |", (A[0]<A[1]<A[2]) or (A[0]>A[1]>A[2]))


def bool23():
    A = input("Введите число> ")
    print("Слева направо = справо налево? |", A==A[::-1])


def bool24():
    a, b, c = float(input("A = ")), float(input("B = ")), float(input("C = "))
    D = (b**2 - 4*a*c)**0.5

    x1 = (-b + D)/(2*a)
    x2 = (-b - D) / (2 * a)

    print("имеет вещественные корни?", (type(x1)==complex)or(type(x2)==complex))

def main():
    bool24()


if __name__ == "__main__":
    main()