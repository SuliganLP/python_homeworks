"""
Task №1

Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""

text = "My number is 123-456-789"
res_string = ""

for elem in text:
    if elem.isdigit():
        res_string += "*"
    else:
        res_string += elem

print(res_string)


"""
Task №2

Количество символов

Напишите программу, которая подсчитывает количество вхождений всех символов в строке. 
Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. 
Выводите повторяющиеся символы только один раз.

text = "Programming in python"

Пример вывода:

Строка: Programming in python

Символ 'p' встречается 2 раз(а)
Символ 'r' встречается 2 раз(а)
Символ 'o' встречается 2 раз(а)
Символ 'g' встречается 2 раз(а)
Символ 'm' встречается 2 раз(а)
Символ 'i' встречается 2 раз(а)
Символ 'n' встречается 3 раз(а)
Символ ' ' встречается 2 раз(а)
"""

text = "Programming in python"
used = ""

for elem in text.lower():
    if text.lower().count(elem) > 1 and elem not in used:
        print(f"Символ '{elem}' встречается {text.lower().count(elem)} раз(а).")
        used += elem


"""
Task №3

Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
"""


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
new_string = ""

for elem in text.split():
    if elem.isdigit():
        new_string += str(float(elem) * 10) + " "
    elif elem.count(".") == 1 and elem.replace(".", "").isdigit():
        new_string += str(float(elem) * 10) + " "
    else:
        new_string += elem + " "

new_string = new_string.rstrip()
print(new_string)
