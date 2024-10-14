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
        res = " ".join(chr(i) for i in range(65, 65+n))
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
        elif 1040 <= uni <= 1071 or uni == 1025:
            res = "rus"
        print(res)
        return res

    @staticmethod
    def string7(line: str) -> (int, int):
        uni_first, uni_last = ord(line[0]), ord(line[-1])
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
        res = line.swapcase()
        print(res)
        return res

    @staticmethod
    def string27(n1: int, n2: int, s1: str, s2: str) -> str:
        res = s1[:n1] + s2[-n2:]
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
        res = line.count(line2)
        print(res)
        return res

    @staticmethod
    def string33(line: str, line2: str) -> str:
        line = line.replace(line2, "", 1)
        print(line)
        return line

    @staticmethod
    def string36(line: str, line1: str, line2: str) -> str:
        res = line.replace(line1, line2, 1)
        print(res)
        return res

    @staticmethod
    def string39(line: str) -> str:
        s = line.split(" ")
        res = "" if len(s) == 2 else s[1]
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
        res = 0
        for i in parse_arr:
            if i[0] == i[-1]:
                res += 1
        print(res)
        return res

    @staticmethod
    def string46(line: str) -> int:
        max_l = len(max(line.split(), key=len))
        print(max_l)
        return max_l

    @staticmethod
    def string47(line: str) -> str:
        res = ".".join(line.split())
        print(res)
        return res

    @staticmethod
    def string53(line: str) -> int:
        target_symbols = [".", "!", "?", ",", ";", ":", "—", "(", ")", "\"", "»", "«"]
        counter = 0
        for i in target_symbols:
            counter += line.count(i)
        print(counter)
        return counter

    @staticmethod
    def string54(line: str) -> (tuple, list):
        b = ("а", "ё", "у", "е", "ы", "о", "э", "я", "и", "ю")
        line = line.lower()
        counter = 0
        for s in line:
            if s in b:
                counter += 1

        print(counter)
        return counter

    @staticmethod
    def string55(line: str) -> str:
        from re import split as rsplit
        words = rsplit(r"[.!?,;:—()\"»« ]", line)
        max_len = 0
        res = ""
        for i in range(len(words)-1, -1, -1):
            print(words[i])
            tl = len(words[i])
            if tl > max_len:
                max_len = tl
                res = words[i]
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
        i = line.replace("/", "\\").replace("\\\\", "\\", 1).split("\\")
        res = i[1] if len(i) > 2 else "\\"
        print(res)
        return res

    @staticmethod
    def string61(line: str) -> str:
        i = line.replace("/", "\\").replace("\\\\", "\\", 1).split("\\")
        res = i[-2] if len(i) > 2 else "\\"
        print(res)
        return res

    @staticmethod
    def string62(line: str) -> str:
        res = ""
        for el in line:
            i_char = ord(el)
            if 1071 < i_char < 1104:
                s = "а" if i_char + 1 == 1104 else chr(i_char + 1)
            elif 1039 < i_char < 1072:
                s = "А" if i_char+1 == 1072 else chr(i_char+1)
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

    # @staticmethod
    # def string70(line: str) -> int:
    #     open_brackets = 0
    #     close_brackets = 0
    #     for op_b, cl_b in (("(", ")"), ("[", "]"), ("{", "}")):
    #         for i in line:
    #             if i == op_b:
    #                 open_brackets += 1
    #             elif i == cl_b:
    #                 close_brackets += 1
    #         if open_brackets > close_brackets:
    #             return -1
    #         brackets = 0
    #         for i, char in enumerate(line):
    #             if char == op_b:
    #                 brackets += 1
    #             elif char == cl_b:
    #                 brackets -= 1
    #             if brackets < 0:
    #                 return i+1
    #     return 0

    @staticmethod
    def string70(line: str) -> int:
        counter = [0, 0, 0]
        for i, v in enumerate(line):
            match v:
                case "(":
                    counter[0] += 1
                case ")":
                    counter[0] -= 1
                    if counter[0] < 0:
                        return i+1
                case "[":
                    counter[1] += 1
                case "]":
                    counter[1] -= 1
                    if counter[1] < 0:
                        return i+1
                case "{":
                    counter[2] += 1
                case "}":
                    counter[2] -= 1
                    if counter[2] < 0:
                        return i + 1
        for i in counter:
            if i > 0:
                return -1
        return 0


# 3 4 6 7 8 13 18 27 30 31 32 33 36 39 41 42 46 47 53 54 55 57 58 59 60 61 62 66 67 70
if __name__ == "__main__":
    pass
    # StringsTask.string3("")
    # StringsTask.string13("werw3204wfggewt34563gertert")
    # StringsTask.string18("ЁжИк.")
    # StringsTask.string27(0, 4, "Hello", "Кукуtester")
    # StringsTask.string30("s", "test test", "pop")
    # StringsTask.string31("Привет всем, друзья!", "всё")
    # StringsTask.string32("ку ку ку", "ку")
    # StringsTask.string33("Ку ку ку ку хех", "кE")
    # StringsTask.string36("друзья, ну всем пока, друзья", "друзья", "ребята")
    # StringsTask.string39("message test ")
    # StringsTask.string41("adasd 2rr2      werwerwer    2452345")
    # StringsTask.string42("ПРИВЕТ ПРИВЕТ КУКУ АДАМА ВУАЛЬ УМЕНИЕ АВРААМ ТПОФИГИСТ")
    # StringsTask.string46("ПРИВЕТ ПРИВЕТ КУКУ АДАМ ВУАЛЬ УМЕНИЕ АВРААМ ПОФИГИСТ")
    # StringsTask.string47("ПРИВЕТ    ПРИВЕТ КУКУ АДАМ ВУАЛЬ       УМЕНИЕ АВРААМ  ПОФИГИСТ")
    # StringsTask.string54("ёуеыаоэяиюЁУЕЫАОЭЯИЮВ")
    # StringsTask.string55("ПРИВЕТ, ТDОФИГИСТ ПРИВЕТ.КУКУ(АДАМА)ВУАЛЬ УМЕНИЕ \"АВРААМ\"; ТПОФИГИСТ. d")
    # StringsTask.string61("C:\\\\OpenVPNPortable_1.6.6.paf.exe")
    # StringsTask.string62("абвгдежзийклмнопрстуфхцчшщъыьэюя".upper())
    # StringsTask.string62("абвгдежзийклмнопрстуфхцчшщъыьэюя")
    # x = StringsTask.string66("Программа")
    # StringsTask.string67(x)
    # StringsTask.string67(x)
    # print(StringsTask.string70("{{}}(()){}"))
    # StringsTask.string32("Hello hi hi hihi Hello ihihello", "hi")
    # StringsTask.string55("Кто,постучал  в   дверь.")
