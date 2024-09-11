"""
tasks from https://www.ptaskbook.com/en/tasks/string.php
3 4 6 7 8 13 18 27 30 31 32 33 36 39 41 42 46 47 53 54 55 57 58 59 60 61 62 66 67 70
"""

from math import floor, ceil


class StringsTask:
    @staticmethod
    def string3(char: str) -> (str, str):
        uni = ord(char)
        before, after = chr(uni-1), chr(uni+1)
        print(before, after)
        return before, after

    @staticmethod
    def string4(n: int) -> str:
        res = chr(64+n)
        print(res)
        return res

    @staticmethod
    def string6(char: str) -> str:
        uni = ord(char.upper())
        res = "Что-то странное получилось"
        if 48 <= uni <= 57:
            res = "digit"
        elif 65 <= uni <= 90:
            res = "lat"
        elif 1040 <= uni <= 1071:
            res = "rus"
        print(res)
        return res

    @staticmethod
    def string7(line: str) -> (int, int):
        uni_first, uni_last = ord(line[0]), ord(line[len(line)-1])
        print(uni_first, uni_last)
        return uni_first, uni_last

    @staticmethod
    def string8(n: int, char: str) -> str:
        res = char * n
        print(res)
        return res

    @staticmethod
    def string13(line: str) -> int:
        counter = 0
        for i in line:
            if i.isdigit():
                counter += 1
        print(counter)
        return counter

    @staticmethod
    def string18(line: str) -> str:
        res = "".join([_.upper() if _.islower() else _.lower() for _ in line])
        print(res)
        return res

    @staticmethod
    def string27(n1: int, n2: int, s1: str, s2: str) -> str:
        res = s1[:n1] + s2[n2+1:]
        print(res)
        return res

    @staticmethod
    def string30(char: str, line: str, line2: str) -> str:
        line = line.replace(char, char+line2)
        print(line)
        return line

    @staticmethod
    def string31(line: str, line2: str) -> int:
        res = False if line.find(line2) == -1 else True
        print(res)
        return res

    @staticmethod
    def string32(line: str, line2: str) -> int:
        res = len(line.split(line2))-1
        print(res)
        return res

    @staticmethod
    def string33(line: str, line2: str) -> str:
        line = line.replace(line2, "", 1)
        print(line)
        return line

    @staticmethod
    def string36(line: str, line1: str, line2: str) -> str:
        res = line.replace(line1, line2)
        print(res)
        return res

    @staticmethod
    def string39(line: str) -> str:
        s = line.split(" ")
        if len(s) < 3:
            res = line
        else:
            res = s[1]
        print(res)
        return res

    @staticmethod
    def string41(line: str) -> int:
        res = len(line.split())
        print(res)
        return res

    @staticmethod
    def string42(line: str) -> int:
        parse_arr = line.split()
        counter = {}
        for i in parse_arr:
            ekey = i[0] + i[-1]
            val = counter.get(ekey)
            if val is None:
                val = 0
            val += 1
            counter[ekey] = val

        res = max(list(counter.values()))
        print(res)
        return res

    @staticmethod
    def string46(line: str) -> int:
        parse_arr = line.split()
        max_length = -1
        for i in parse_arr:
            length = len(i)
            if length > max_length:
                max_length = length

        print(max_length)
        return max_length

    @staticmethod
    def string47(line: str) -> str:
        res = ".".join(line.split())
        print(res)
        return res

    @staticmethod
    def string53(line: str) -> int:
        target_symbols = ",.?!;:\'\""
        counter = 0
        for i in target_symbols:
            counter += line.count(i)
        print(counter)
        return counter

    @staticmethod
    def string54(line: str) -> (tuple, list):
        b = ("а", "ё", "у", "е", "ы", "о", "э", "я", "и", "ю")
        c = [0 for _ in b]
        for s in line:
            f_symbol = s.lower()
            for index, value in enumerate(b):
                if value == f_symbol:
                    c[index] += 1
                    break

        print("", *list(f"{b[i]}: {c[i]}\n" for i in range(len(b))))
        return b, c

    @staticmethod
    def string55(line: str) -> int:
        cleaned_sentence = ''.join(char if char.isalpha() or char.isspace() else '' for char in line)
        words = cleaned_sentence.split()
        res = len(max(words, key=len))
        print(res)
        return res

    @staticmethod
    def string57(line: str) -> str:
        res = " ".join(line.split())
        print(res)
        return res

    @staticmethod
    def string58(line: str) -> str:
        res = ".".join(line.replace("/", "\\").split("\\")[-1].split(".")[:-1])
        print(res)
        return res

    @staticmethod
    def string59(line: str) -> str:
        res = line.replace("/", "\\").split("\\")[-1].split(".")[-1]
        print(res)
        return res

    @staticmethod
    def string60(line: str) -> str:
        i = line.replace("/", "\\").split("\\")
        res = i[1] if len(i) > 2 else "/"
        print(res)
        return res

    @staticmethod
    def string61(line: str) -> str:
        i = line.replace("/", "\\").split("\\")
        res = i[-2] if len(i) > 2 else "/"
        print(res)
        return res

    @staticmethod
    def string62(line: str) -> str:
        f = line.replace("ё", "е").replace("Ё", "Е")
        res = ""
        for el in f:
            if 1071 < ord(el) < 1104:
                s = "а" if ord(el)+1 == 1104 else chr(ord(el)+1) if ord(el) != 1077 else "ж"
            elif 1040 < ord(el) < 1072:
                s = "А" if ord(el)+1 == 1072 else chr(ord(el)+1) if ord(el) != 1045 else "Ж"
            else:
                s = el
            res += s
        print(res)
        return res

    @staticmethod
    def string66(line: str) -> str:
        s1 = "".join(line[i] for i in range(1, len(line), 2))
        s2 = "".join(reversed(list(line[i] for i in range(0, len(line), 2))))
        res = s1 + s2
        print(res)
        return res

    @staticmethod
    def string67(line: str) -> str:
        s1 = line[:floor(len(line)/2)]
        s2 = line[-ceil(len(line)/2):][::-1]
        res = "".join([s2[i//2] if i % 2 == 0 else s1[(i-1)//2] for i in range(len(line))])
        print(res)
        return res

    @staticmethod
    def string70(line: str) -> int:
        open_brackets = 0
        close_brackets = 0
        for op_b, cl_b in (("(", ")"), ("[", "]"), ("{", "}")):
            for i in line:
                if i == op_b:
                    open_brackets += 1
                elif i == cl_b:
                    close_brackets += 1
            if open_brackets > close_brackets:
                return -1
            brackets = 0
            for i, char in enumerate(line):
                if char == op_b:
                    brackets += 1
                elif char == cl_b:
                    brackets -= 1
                if brackets < 0:
                    return i
        return 0


if __name__ == "__main__":
    pass
    # StringsTask.string3("ы")
    # StringsTask.string7("easy test")
    # StringsTask.string13("werw324wfggewt34563gertert")
    # StringsTask.string18("ПриВет")
    # StringsTask.string27(3, 4, "Hello", "Кукуtester")
    # StringsTask.string30("s", "test test", "pop")
    # StringsTask.string31("Привет всем, друзья!", "все")
    # StringsTask.string32("ку ку ку", "ку")
    # StringsTask.string33("Ку ку ку ку хех", "ку")
    # StringsTask.string36("ну всем пока, друзья", "друзья", "ребята")
    # StringsTask.string39("message test")
    # StringsTask.string41("adasd 2rr2  werwerwer    2452345")
    # StringsTask.string42("ПРИВЕТ ПРИВЕТ КУКУ АДАМ ВУАЛЬ УМЕНИЕ АВРААМ ПОФИГИСТ")
    # StringsTask.string46("ПРИВЕТ ПРИВЕТ КУКУ АДАМ ВУАЛЬ УМЕНИЕ АВРААМ ПОФИГИСТ")
    # StringsTask.string47("ПРИВЕТ    ПРИВЕТ КУКУ АДАМ ВУАЛЬ       УМЕНИЕ АВРААМ  ПОФИГИСТ")
    # StringsTask.string54(test_text)
    # StringsTask.string62("абвгдежзийклмнопрстуфхцчшщъыьэюя".upper())
    # StringsTask.string62("абвгдежзийклмнопрстуфхцчшщъыьэюя")
    # x = StringsTask.string66("Программа")
    # print(StringsTask.string67_1(x))
    # x = StringsTask.string66("Программа")
    # StringsTask.string67(x)
    # print(StringsTask.string70("[]][[]"))
