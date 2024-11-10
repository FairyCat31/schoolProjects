from _io import TextIOWrapper
from re import split as rsplit
import math
from collections import OrderedDict


def text1(filename: str, n: int, k: int):
    line = "*" * k
    with open(filename, "a") as f:
        for _ in range(n):
            f.write(line)


def text2(filename: str, n: int):
    lines = ["a"]
    for i in range(1, n):
        lines.append(lines[-1]+chr(97+i))
    text = "\n".join(lines)
    with open(filename, "w") as f:
        f.write(text)


def text3(filename: str, n: int):
    lines = ["A"]
    for i in range(1, n):
        lines.append(lines[-1] + chr(65 + i))
    for i in range(len(lines)):
        lines[i] = f"{lines[i]:*<{n}}"
    text = "\n".join(lines)
    with open(filename, "w") as f:
        f.write(text)


def text5(s: str, file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "a") as f:
        f.write(s)


def text6(file1: TextIOWrapper, file2: TextIOWrapper):
    file1.writelines(file2.readlines())


def text7(s: str, file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "r") as f:
        lines = f.readlines()
        lines.insert(0, s+"\n")
    with open(filename, "w") as f:
        f.writelines(lines)


def text8(file1: TextIOWrapper, file2: TextIOWrapper):
    filename1 = file1.name
    file1.close()
    filename2 = file2.name
    file2.close()
    with open(filename1, "r") as f1, open(filename2, "r") as f2:
        lines = f2.readlines() + f1.readlines()
    with open(filename1, "w") as f:
        f.writelines(lines)


def text9(k: int, file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "r") as f:
        lines = f.readlines()
    if len(lines) < k:
        return
    lines.insert(k-1, "\n")
    with open(filename, "w") as f:
        f.writelines(lines)


def text10(k: int, file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "r") as f:
        lines = f.readlines()
    if len(lines) < k:
        return
    lines.insert(k, "\n")
    with open(filename, "w") as f:
        f.writelines(lines)


def text13(file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        f.writelines(lines[1:])


def text14(file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        f.writelines(lines[:-1])


def text15(k: int, file: TextIOWrapper):
    filename = file.name
    file.close()
    with open(filename, "r") as f:
        lines = f.readlines()
    if len(lines) < k:
        return
    lines.pop(k-1)
    with open(filename, "w") as f:
        f.writelines(lines)


def text30(file: TextIOWrapper):
    # file: open("путь/до/файла", "r") Важно !!!! В функцию передавать только файл с модом R
    lines = file.readlines()
    word = ""
    l = float("inf")
    for i in lines:
        for w in i.split():
            w_l = len(w)
            if w_l <= l:
                l = w_l
                word = w
    print(word)


def text31(k: int, file: TextIOWrapper):
    # file: open("путь/до/файла", "r") Важно !!!! В функцию передавать только файл с модом R
    lines = file.readlines()
    words = []
    for i in lines:
        for w in rsplit(r"[.!?,;:—()\"»« ]", i):
            if len(w) == k:
                words.append(w + "\n")
    with open("output.txt", "w") as f:
        f.writelines(words)


def text32(c: str, file: TextIOWrapper):
    # file: open("путь/до/файла", "r") Важно !!!! В функцию передавать только файл с модом R
    lines = file.readlines()
    words = []
    for i in lines:
        for w in rsplit(r"[.!?,;:—()\"»« ]", i):
            if w[0].upper() == c:
                words.append(w + "\n")
    with open("output.txt", "w") as f:
        f.writelines(words)


def text33(c: str, file: TextIOWrapper):
    # file: open("путь/до/файла", "r") Важно !!!! В функцию передавать только файл с модом R
    lines = file.readlines()
    words = []
    for i in lines:
        for w in rsplit(r"[.!?,;:—()\"»« ]", i):
            if c in w.lower():
                words.append(w + "\n")
    with open("output.txt", "w") as f:
        f.writelines(words)


def text43(a: float, b: float, n: int, filename='trig_table.txt'):
    step = (b - a) / n
    with open(filename, 'w') as f:
        f.write(f"{'x':>8} {'sin(x)':>12} {'cos(x)':>12}\n")
        for i in range(n + 1):
            x = a + i * step
            sin_x = math.sin(x)
            cos_x = math.cos(x)
            f.write(f"{x:>8.4f} {sin_x:>12.8f} {cos_x:>12.8f}\n")


def text44(filename):
    count = 0
    total_sum = 0

    with open(filename, 'r') as file:
        for line in file:
            number_str = line.strip()
            if number_str:
                number = int(number_str)
                count += 1
                total_sum += number
    print(count, total_sum)


def text54(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    unique_characters = OrderedDict.fromkeys(text)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(''.join(unique_characters.keys()))


def text55(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    unique_chars = set(text)
    sorted_chars = sorted(unique_chars, key=ord)
    with open(output_file, "w", encoding="utf-8") as output_file:
        output_file.write(''.join(sorted_chars))

#TODO: 1-3 5-10 13-15 30-33 43 44 54 55