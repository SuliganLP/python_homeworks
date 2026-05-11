# Класс Person
# Создайте класс Person, представляющий человека.
# ● Каждый человек должен иметь имя.
# ● Добавьте метод introduce(), который выводит приветствие с именем.
# Пример вывода:
# Hello, my name is Alice.

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"Hello, my name is {self.name}."


pers_1 = Person("Alice")
print(pers_1.introduce())


# Класс Student
# На основе класса Person создайте класс Student.
# ● Студент должен иметь имя и номер курса.
# ● Метод introduce() должен сначала выводить базовое приветствие, а затем
# строку: I'm on course <номер_курса>.
# Пример вывода:
# Hello, my name is Alice.
# I'm on course 2.

class Student(Person):
    def __init__(self, name: str, course_num: int) -> None:
        super().__init__(name)
        self.course_num = course_num

    def introduce(self) -> str:
        return f"{super().introduce()}\nI'm on course {self.course_num}."


stud_1 = Student("Alex", 7)
stud_2 = Student("John", 3)

print(stud_1.introduce())
print(stud_2.introduce())


# Класс Teacher и список людей
# На основе класса Person создайте класс Teacher.
# ● У преподавателя есть имя и предмет.
# ● Метод introduce() должен выводить имя и предмет.
# ● Метод introduce() должен выводить строку: Hello, I am professor <имя>.
# My subject is <предмет>.
# ● Создайте список, в котором будут Student и Teacher, и вызовите у всех метод
# introduce().
# Пример вывода:
# Hello, my name is Alice.
# I'm on course 2.
# Hello, I am professor Bob.
# My subject is Mathematics

class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def introduce(self) -> str:
        return f"Hello, I am professor {self.name}.\nMy subject is {self.subject}."


people = [Student("Alex", 7), Teacher("John", "Computer Science")]

for person in people:
    print(person.introduce())
