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
    def array2(n: int) -> List[int]:
        arr = []
        for i in range(1, n+1):
            arr.append(2**i)
        return arr

    @staticmethod
    def array5(n: int) -> List[int]:
        return [SubFuncs.fibonacci_of(i) for i in range(1, n+1)]

    @staticmethod
    def array8(arr: List[int]) -> str:
        result = ""
        counter = 0
        for i in arr:
            if i % 2:
                counter += 1
                result += f"{i} "
        result += f"count={counter}"
        return result

    @staticmethod
    def array10(arr: List[int]) -> (List[int], List[int]):
        result = []
        for i in arr:
            if i % 2:
                result.insert(0, i)
                continue
            result.append(i)
        return result

    @staticmethod
    def array11(arr: list, k: int) -> List[Any]:
        result = []
        for i in range(k-1, len(arr), k):
            result.append(arr[i])
        return result

    @staticmethod
    def array19(arr: List[int]) -> int:
        min_arr = arr[0]
        max_arr = arr[9]
        res = 0
        for i in range(1, 9):
            if min_arr < arr[i] < max_arr:
                res = i+1

        return res

    @staticmethod
    def array21(arr: List[int], from_num: int, to_num: int) -> float:
        if from_num == to_num:
            return arr[from_num-1]
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
        for i in range(0, from_num-1):
            nums += arr[i]
            counter += 1

        for i in range(to_num, len(arr)):
            nums += arr[i]
            counter += 1
        res = nums / counter

        return res

    @staticmethod
    def array24(arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
        difference = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if difference != arr[i] - arr[i-1]:
                difference = 0
                break
        return difference

    @staticmethod
    def array27(arr: List[int]) -> int:
        switch = 1 if arr[0] > 0 else 0
        for i in range(1, len(arr)):
            if switch and arr[i] < 0:
                switch = 0
                continue
            elif not switch and arr[i] > 0:
                switch = 1
                continue
            else:
                return i+1
        return 0

    @staticmethod
    def array29(arr: List[int]) -> int:
        max_num = arr[0]
        for i in range(1, len(arr), 2):
            if arr[i] > max_num:
                max_num = arr[i]

        return max_num

    @staticmethod
    def array42(arr: List[int], r: int) -> (int, int):
        min_n = arr[0]
        max_n = arr[1]
        difference = abs(r - (min_n+max_n))
        for i in range(1, len(arr)):
            new_diff = abs(r - (arr[i]+arr[i-1]))
            if new_diff < difference:
                difference = new_diff
                min_n, max_n = arr[i-1], arr[i]
        return min_n, max_n

    @staticmethod
    def array47(arr: List[int]) -> int:
        nums = []
        for i in arr:
            if i in nums:
                continue
            nums.append(i)
        return len(nums)

    @staticmethod
    def array48(arr: List[int]) -> int:
        result = -1
        for i in arr:
            count = arr.count(i)
            if count > result:
                result = count
        return result

    @staticmethod
    def array52(arr: List[int]) -> List[float | int]:
        result = []
        for i in arr:
            if i < 5:
                result.append(i * 2)
                continue
            result.append(i / 2)
        print(result)
        return result

    @staticmethod
    def array53(arr: List[float | int], arr2: List[float | int]) -> List[int | float]:
        result = []
        for i in range(len(arr)):
            t = max(arr[i], arr2[i])
            result.append(t)
        print(result)
        return result

    @staticmethod
    def array65(arr: List[int], k: int) -> None:
        mod = arr[k-1]
        for i in range(len(arr)):
            arr[i] *= mod

    @staticmethod
    def array68(arr: List[float | int]) -> None:
        min_v = min(arr)
        max_v = max(arr)
        min_i = arr.index(min_v)
        max_i = arr.index(max_v)
        arr[min_i], arr[max_i] = max_v, min_v

    @staticmethod
    def array69(arr: list) -> None:
        for i in range(0, len(arr), 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    @staticmethod
    def array79(arr: list) -> None:
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = 0

    @staticmethod
    def array83(arr: list) -> None:
        last_i = len(arr)-1
        last = arr[last_i]
        for i in range(last_i, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last

    @staticmethod
    def array87(arr: list) -> None:
        num = arr[0]
        del arr[0]
        for i in range(len(arr)):
            if arr[i] > num:
                arr.insert(i, num)
                break

    @staticmethod
    def array90(arr: list, k: int) -> None:
        del arr[k-1]

    @staticmethod
    def array91(arr: list, from_num: int, to_num: int) -> None:
        for _ in range(from_num - 1, to_num+1):
            del arr[from_num-1]
        print(len(arr), arr)

    @staticmethod
    def array96(arr: list) -> None:
        mod = 0
        nums = []
        for i in range(len(arr)):
            k = i-mod
            if arr[k] in nums:
                del arr[k]
                mod += 1
                continue
            nums.append(arr[k])

    @staticmethod
    def array102(arr: list, k: int) -> None:
        arr.insert(k, 0)


if __name__ == "__main__":
    pass
    # ArraysTask.array11([3, 4, 65, 654, 35, 65, 3643, 66, 676, 73, 33], 3)
    # ArraysTask.array27([-2, 1, -2, 4, -5, 5, -8])
    # ArraysTask.array47([3, 1, 4, 65, 654, 35, 65, 3643, 66, 676, 73, 33, 1, 2], 3)
    # ArraysTask.array48([3, 1, 1, 2, 2, 2])
    # ArraysTask.array87([3, 1, 2, 3, 4, 5, 6, 7])
    # ArraysTask.array102([1, 2, 4, 5], 3)
    # test = [1, 4, 21, 3, 5, -7, 9, 1, 15, 15, 11, -13, 15, 17]
    # test = [6, -2, 3, 0, 1, 2, 3, 8, 9, -2, 0, 0, 20]
    # ArraysTask.array102(test, 3)
    # print(test)
