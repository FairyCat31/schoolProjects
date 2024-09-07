"""
Tasks from http://www.ptaskbook.com/ru/tasks/array.php
2 5 8 10 11 19 21 23 24 27 29 42 47 48 52 53 65 68 69 79 83 87 90 91 96 102
"""
from typing import Any, List


class SubFuncs:
    @staticmethod
    def fibonacci_of(n):
        if n in {0, 1}:
            return n
        return SubFuncs.fibonacci_of(n - 1) + SubFuncs.fibonacci_of(n - 2)


class ArraysTask:

    @staticmethod
    def set_n(func):
        def wrapper(*args, **kwargs):
            num = int(input("N > "))
            result: Any = func(n=num, *args, **kwargs)
            print(result)
        return wrapper

    @staticmethod
    @set_n
    def array2(n: int) -> List[int]:
        arr = []
        for i in range(1, n*2, 2):
            arr.append(i)
        return arr

    @staticmethod
    @set_n
    def array5(n: int) -> List[int]:
        return [SubFuncs.fibonacci_of(i) for i in range(n)]

    @staticmethod
    def array8(arr: List[int]) -> str:
        res = ""
        counter = 0
        for i in arr:
            if i % 2:
                counter += 1
                res += f"{i} "

        res += f"k={counter}"
        print(res)
        return res

    @staticmethod
    def array10(arr: List[int]) -> (List[int], List[int]):
        res = []
        res2 = []
        for i in arr:
            if i % 2:
                res2.append(i)
                continue
            res.append(i)
        res2.reverse()
        print(res)
        print(res2)
        return res, res2

    @staticmethod
    def array11(arr: list, k: int) -> List[Any]:
        res = []
        for i in range(k, len(arr), k):
            res.append(arr[i])
        print(res)
        return res

    @staticmethod
    def array19(arr: List[int]) -> int:
        min_arr = arr[0]
        max_arr = arr[9]
        res = 0
        for i in range(1, 9):
            num = arr[i]
            if min_arr < num < max_arr:
                res = num

        print(res)
        return res

    @staticmethod
    def array21(arr: List[int], from_num: int, to_num: int) -> float:
        nums = 0
        for i in range(from_num - 1, to_num):
            nums += arr[i]
        res = nums / (to_num - from_num)
        print(res)
        return res

    @staticmethod
    def array23(arr: List[int], from_num: int, to_num: int) -> float:
        nums = 0
        counter = 0
        for i in range(0, from_num - 1):
            nums += i
            counter += 1

        for i in range(to_num, len(arr)):
            nums += i
            counter += 1

        res = nums / counter
        print(res)
        return res

    @staticmethod
    def array24(arr: List[int]) -> int:
        if len(arr) < 2:
            print(0)
            return 0
        difference = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if difference != arr[i] - arr[i-1]:
                difference = 0
                break
        print(difference)
        return difference

    @staticmethod
    def array27(arr: List[int]) -> int:
        switch = 1 if arr[0] > 0 else -1
        for i in arr:
            if i*switch > 0:
                switch *= -1
                continue
            print(i)
            return i

        print(0)
        return 0

    @staticmethod
    def array29(arr: List[int]) -> int:
        max_num = None
        arr.sort()
        arr.reverse()
        for i in arr:
            if i % 2:
                max_num = i
                break
        print(max_num)
        return max_num

    @staticmethod
    def array42(arr: List[int], r: int) -> (int, int):
        min_n = arr[0]
        max_n = arr[1]
        difference = abs(r - (min_n+max_n))
        for i in range(1, len(arr)):
            if abs(r - (arr[i]+arr[i-1])) < difference:
                min_n, max_n = arr[i-1], arr[i]

        print(min_n, max_n)
        return min_n, max_n

    @staticmethod
    def array47(arr: List[int]) -> int:
        nums = []
        for i in arr:
            if i in nums:
                continue
            nums.append(i)
        res = len(nums)
        print(res)
        return res

    @staticmethod
    def array48(arr: List[int]) -> int:
        res = -1
        for i in arr:
            count = arr.count(i)
            if count > res:
                res = count
        print(res)
        return res

    @staticmethod
    def array52(arr: List[int]) -> List[float | int]:
        res = []
        for i in arr:
            if i < 5:
                res.append(i*2)
                continue
            res.append(i/2)
        print(res)
        return res

    @staticmethod
    def array53(arr: List[float | int], arr2: List[float | int]) -> List[int | float]:
        res = []
        for i in range(len(arr)):
            t = max(arr[i], arr2[i])
            res.append(t)
        print(res)
        return res

    @staticmethod
    def array65(arr: List[int], k: int) -> List[int]:
        res = list([i*arr[k-1] for i in arr])
        print(res)
        return res

    @staticmethod
    def array68(arr: List[float | int]) -> List[float | int]:
        min_v = min(arr)
        max_v = max(arr)
        min_i = arr.index(min_v)
        max_i = arr.index(max_v)
        res = arr.copy()
        res[min_i], res[max_i] = max_v, min_v
        print(res)
        return res

    @staticmethod
    def array69(arr: list) -> list:
        res = []
        for i in range(0, len(arr), 2):
            res.append(arr[i+1])
            res.append(arr[i])
        print(res)
        return res

    @staticmethod
    def array79(arr: list) -> list:
        res = arr.copy()
        arr_len = len(res)
        res.insert(0, 0)
        del res[arr_len]
        print(res)
        return res

    @staticmethod
    def array83(arr: list) -> list:
        res = arr.copy()
        last_el_id = len(res)-1
        last_el = res[last_el_id]
        del res[last_el_id]
        res.insert(0, last_el)
        print(res)
        return res

    @staticmethod
    def array87(arr: list) -> list:
        arr.sort()
        print(arr)
        return arr

    @staticmethod
    def array90(arr: list, k: int) -> list:
        del arr[k-1]
        print(arr)
        return arr

    @staticmethod
    def array91(arr: list, from_num: int, to_num: int) -> list:
        for i in range(from_num - 1, to_num):
            del arr[i]
        print(arr)
        return arr

    @staticmethod
    def array96(arr: list) -> list:
        res = []
        for i in arr:
            if i in res:
                continue
            res.append(i)
        print(res)
        return res

    @staticmethod
    def array102(arr: list, k: int) -> list:
        arr.insert(k, 0)
        print(arr)
        return arr


if __name__ == "__main__":
    # ArraysTask.array11([3, 4, 65, 654, 35, 65, 3643, 66, 676, 73, 33], 3)
    # ArraysTask.array27([-2, 1, -2, 4, -5, 5, -8])
    # ArraysTask.array47([3, 1, 4, 65, 654, 35, 65, 3643, 66, 676, 73, 33, 1, 2], 3)
    # ArraysTask.array48([3, 1, 1, 2, 2, 2])
    # ArraysTask.array87([3, 1, 2, 3, 4, 5, 6, 7])
    ArraysTask.array102([1, 2, 4, 5], 3)
