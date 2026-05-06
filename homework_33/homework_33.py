# Среднее время выполнения
# создайте декоратор measure_time, который измеряет и выводит среднее время
# выполнения функции за 5 вызовов.
# Функция может быть любой: например, сортировка списка, чтение из файла или
# расчёты.
# Пример применения:
# @measure_time
# def compute():
#  total = 0
#  for i in range(10_000_000):
#  total += i
#  return total
# Пример вывода:
# Среднее время выполнения для 5 вызовов:
# 0.21 секунд
# Результат: 49999995000000
from functools import wraps
from time import time


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        total_time = 0
        result = None

        for _ in range(5):
            start = time()
            result = func(*args, *kwargs)
            end = time()
            total_time += end - start

        average_time = total_time / 5

        print(f"Среднее время выполнения для 5 вызовов:")
        print(f"{average_time:.2f} секунд")
        print(f"Результат:", result)
        return result

    return wrapper


@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()


# Среднее время выполнения с количеством вызовов
# доработайте декоратор measure_time, чтобы он принимал параметр repeats —
# количество вызовов функции.
# Декоратор должен выполнять функцию указанное число раз и выводить среднее
# время выполнения.
# Пример вывода:
# Среднее время выполнения для 10 вызовов:
# 0.21 секунд
# Результат: 49999995000000
# Пример применения:
# @measure_time(10)
# def compute():
#  total = 0
#  for i in range(10_000_000):
#  total += i
#  return total
#
def measure_time(repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None

            for _ in range(repeats):
                start = time()
                result = func(*args, **kwargs)
                end = time()
                total_time += end - start

            average_time = total_time / repeats

            print(f"Среднее время выполнения для {repeats} вызовов:")
            print(f"{average_time:.2f} секунд")
            print(f"Результат:", result)
            return result

        return wrapper

    return decorator


@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()
