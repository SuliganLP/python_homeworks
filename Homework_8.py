"""Проверка кодировки
Напишите программу, которая принимает от пользователя один символ и выводит его код в таблице Unicode
и его принадлежность к диапазону ASCII (True/False).
Пример вывода:
Введите символ: A
Код Unicode: 65
ASCII символ: True"""

# user_input = input("Введите символ: ")
#
# print(f"Код Unicode: {ord(user_input)}")
# print(f"ASCII символ: {user_input.isascii()}")


"""Подстрока с заполнением
Напишите программу, которая принимает строку и индексы начала и конца. 
Программа должна вывести подстроку на указанных позициях. 
Также если конечный индекс выходит за пределы строки, программа заполняет недостающие символы символами _.

Пример вывода:
Введите строку: Программирование  
Введите начальный индекс: 3  
Введите конечный индекс: 20  
Подстрока: граммирование_____"""

# user_string = input("Введите строку: ")
# user_start_index = int(input("Введите начальный индекс: "))
# user_end_index = int(input("Введите конечный индекс: "))
#
# user_string_sliced = user_string[user_start_index:user_end_index]
# underline_counter = (user_end_index - user_start_index) - len(user_string_sliced)
#
# if underline_counter > 0:
#     user_string_sliced += "_" * underline_counter
# print(f"Подстрока: {user_string_sliced}")


"""Напишите программу, которая принимает строку и символ, а затем подсчитывает, сколько раз символ встречается в строке.
Пример вывода:
Введите строку: Hello, world!  
Введите символ: o  
Символ o встречается 2 раз(а)."""

# from time import sleep
#
#
# user_input_string = input("Введите строку: ")
# user_input_char = input("Введите символ: ")
#
# if len(user_input_char) != 1 or user_input_string == "":
#     print("Критическая ошибка. Запущен процесс самоуничтожения...")
#     sleep(1)
#     print("3")
#     sleep(1)
#     print("2")
#     sleep(1)
#     print("1")
#     sleep(3)
#     print("Шутка. Попробуй еще раз.")
# else:
#     char_count = user_input_string.count(user_input_char)
#     print(f"Символ {user_input_char} встречается {char_count} раз.")

"""Напишите программу, которая принимает строку и выводит её в обратном порядке, пропуская все цифры.

Пример вывода:
Введите строку: n52uFs6Inoh67ty8P
Результат: PythonIsFun"""

# 
# user_input = input("Введите строку: ")
# result_string = ""
#
# for char in user_input:
#     if char.isalpha():
#         result_string += char
#
# print(f"Результат: {result_string[::-1]}")
