class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def __str__(self):
        return f"Я {self._first_name} {self._last_name}\nМне {self._age} лет"

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_age(self) -> int:
        return self._age

    def get_all_parameters(self) -> (str, str, int):
        return self._first_name, self._last_name, self._age

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    def set_age(self, age: int):
        if age > 0:
            self._age = age
            return "Ok"

        return "Ошибка! Возраст указан не верно"


class Employee(Person):
    def __init__(self, job: str, first_name: str, last_name: str, age: int):
        self._job = job
        self._time_in_hours = 10
        super().__init__(first_name, last_name, age)

    def get_all_parameters(self) -> (str, str, int, str, int):
        return *super().get_all_parameters(), self._job, self._time_in_hours

    def chill(self, time: int = 1):
        self._time_in_hours += time
        while self._time_in_hours > 23:
            self._time_in_hours -= 24

    def do_work(self):
        if 9 < self._time_in_hours < 18:
            self.chill()
            print("Я отработал")
            return

        print("Сейчас не подходящее время работать")


class Student(Person):
    def __init__(self, num_class: int, first_name: str, last_name: str, age: int):
        self._num_class = num_class
        self._time_in_hours = 8
        super().__init__(first_name, last_name, age)

    def get_all_parameters(self) -> (str, str, int, int, int):
        return *super().get_all_parameters(), self._num_class, self._time_in_hours

    def get_class(self) -> int:
        return self._num_class

    def set_class(self, new_class: int):
        if self._num_class < new_class < 12:
            self._num_class = new_class

        print("Я не могу задать такой класс")

    def chill(self, time: int = 2):
        self._time_in_hours += time
        while self._time_in_hours > 23:
            self._time_in_hours -= 24

    def do_study(self):
        if 7 < self._time_in_hours < 14:
            self.chill()
            print("Я поучился")
            return

        print("Я не могу сейчас учиться")

    def do_homework(self):
        if 14 < self._time_in_hours < 18:
            self.chill(time=1)
            print("Я сделал часть домашки")
            return

        print("Я не могу сейчас делать домашку")


p = Person("bob", "albertov", 20)
print(p.get_all_parameters())

s = Student(2, *p.get_all_parameters())
print(s.get_class())
print(s.get_all_parameters())
s.do_study()
print(s.get_all_parameters())
s.do_homework()
s.chill(6)
s.do_homework()
print(s.get_all_parameters())


e = Employee("сантехник", *p.get_all_parameters())
print(e.get_all_parameters())
for i in range(9): e.do_work()
print(e.get_all_parameters())
e.chill(16)
print(e.get_all_parameters())
e.do_work()
print(e.get_all_parameters())

