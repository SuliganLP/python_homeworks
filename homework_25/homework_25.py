# Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и
# обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.
import logging


def division(first_num: float, second_num: float) -> float:
    return round(first_num / second_num, 2)


try:
    first_num = float(input("Введите делимое: "))
    second_num = float(input("Введите делитель: "))
    result = division(first_num, second_num)
except ZeroDivisionError:
    print("Делитель не может быть 0")
except ValueError:
    print("Некорректное число")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена")


# Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом
# ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
)


def division(first_num: float, second_num: float) -> float:
    return round(first_num / second_num, 2)


try:
    first_num = float(input("Введите делимое: "))
    second_num = float(input("Введите делитель: "))
    result = division(first_num, second_num)
except ZeroDivisionError:
    logging.error("Делитель не может быть 0")
except ValueError:
    logging.error("Некорректное число")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена")
