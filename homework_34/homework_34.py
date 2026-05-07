# Класс Rectangle
# создайте класс Rectangle, который описывает прямоугольник.
# ● У каждого объекта должны быть два поля: width и height.
# ● Добавьте метод get_area(), который возвращает площадь прямоугольника.
# ● Создайте объект прямоугольника с произвольными значениями.
# ● Выведите его площадь.
# ● Измените ширину и высоту.
# ● Выведите новую площадь.
# Пример вывода:
# Площадь: 20
# Новая площадь: 35


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


rectangle_1 = Rectangle(10, 2)
print(f"Площадь: {rectangle_1.get_area()}")

rectangle_1.width = 15
rectangle_1.height = 3

print(f"Новая площадь: {rectangle_1.get_area()}")

# Класс Counter
# реализуйте класс Counter, который представляет собой простой счётчик.
# ● Счётчик должен начинаться с нуля.
# ● Предусмотрите методы для увеличения и уменьшения значения на единицу, при
# этом при каждой операции должно отображаться новое значение счётчика.
# ● Добавьте метод, возвращающий текущий результат.
# ● Проверьте работу счётчика, выполнив несколько операций.
# Пример вывода:
# Значение увеличено, текущее: 1
# Значение увеличено, текущее: 2
# Значение увеличено, текущее: 3
# Значение уменьшено, текущее: 2
# Текущее значение: 2


class Counter:
    def __init__(self):
        self.value = 0

    def increase_value(self):
        self.value += 1
        return f"Значение увеличено, текущее: {self.value}"

    def decrease_value(self):
        self.value -= 1
        return f"Значение уменьшено, текущее: {self.value}"

    def get_current_value(self):
        return self.value


my_counter = Counter()

print(my_counter.increase_value())
print(my_counter.increase_value())
print(my_counter.increase_value())
print(my_counter.decrease_value())
print(f"Текущее значение: {my_counter.get_current_value()}")
