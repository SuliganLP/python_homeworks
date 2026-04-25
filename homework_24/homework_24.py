# # Сумма цифр числа
# # Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# # Пример вывода:
# # 24
#
def sum_digits(num: int) -> int:
    if num < 10:
        return num

    last_digit = num % 10
    remaining_number = num // 10

    return last_digit + sum_digits(remaining_number)


num = 43197
print(sum_digits(num))

# Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]


# Пример вывода:
# 28
def sum_nested_numbers(data: list) -> int:
    total = 0

    for item in data:
        if isinstance(item, list):
            total += sum_nested_numbers(item)
        else:
            total += item

    return total


print(sum_nested_numbers(nested_numbers))
