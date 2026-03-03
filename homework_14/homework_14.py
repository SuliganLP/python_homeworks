""""
Task №1
Число в конце
Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка, 
в которых цифры находятся только в конце.
Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
"""""

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]

new_list = []

for word in strings:
    if word[-1].isdigit() and word.rstrip("123456890").isalpha():
        new_list.append(word)

print(new_list)

""""
Task №2
Удаление кратных
Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
Данные:
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
Пример вывода:
Введите число для удаления кратных ему элементов: 3
Список без кратных значений: [1, 10, 19, 20]
"""""

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
new_list = []

user_input = int(input("Введите число для удаления кратных ему элементов: "))

if user_input == 0:
    print("Ошибка. Число не должно быть 0.")
else:
    for elem in numbers:
        if elem % user_input != 0:
            new_list.append(elem)
    print(f"Список без кратных значений: {new_list}")

""""
Task №3
Порядок четных
Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
нечетные числа занимают те же позиции, чётные числа отсортированы между собой обратном порядке.
Данные:
numbers =                [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]
"""""

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
new_list = []
even_num_list = []

for num in numbers:
    if num % 2 == 0:
        even_num_list.append(num)

even_num_list.sort(reverse=True)
even_counter = 0

for value in numbers:
    if value % 2 == 0:
        new_list.append(even_num_list[even_counter])
        even_counter += 1
    else:
        new_list.append(value)

print(f"Список после сортировки: {new_list}")
