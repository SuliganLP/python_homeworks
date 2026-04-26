# Пример ввода:
# Введите имя файла: text.txt
# Введите количество популярных слов: 3
# Пример вывода:
# Популярные слова:
# python: 4
# is: 3
# in: 2
# Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в файле
# (не учитывая регистр).
# ● Программа запрашивает имя файла и количество популярных слов для вывода.
# ● Если указанный файл не существует, программа должна вывести ошибку.
# Используйте файл text.txt.
import os
from collections import Counter

file_name = input("Введите имя файла: ")

try:
    if not os.path.exists(file_name):
        raise FileNotFoundError
    words_quantity = int(input("Введите количество популярных слов: "))

except FileNotFoundError:
    print(f"Файл {file_name} не найден")

except ValueError:
    print("Количество популярных слов должно быть числом")

else:
    res = []

    with open(file_name, "r", encoding="utf_8") as file:
        for line in file:
            line = line.lower()

            for symbol in ",.!?:;":
                line = line.replace(symbol, "")

            res.extend(line.split())
    total_count = Counter(res).most_common(words_quantity)

    print("Популярные слова: ")

    for key, value in total_count:
        print(f"{key}: {value}")

finally:
    print("Программа завершена")

# 2. Поиск и удаление дубликатов
# напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
# ● Имя нового файла формируется как unique_<original_filename>.
# ● Если файл не существует, программа должна вывести ошибку.
# ● Исходный порядок строк должен сохраниться.
# ● Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.
# Пример ввода:
# Введите имя файла: movies_to_watch.txt
# Пример вывода:
# Дубликаты удалены. Уникальные
# строки сохранены в
# unique_movies_to_watch.txt.

try:
    file_name = input("Введите имя файла: ")

    if not os.path.isfile(file_name):
        raise FileNotFoundError

except FileNotFoundError:
    print(f"Файл не найден")

else:
    res = []
    with open(
            file_name, "r", encoding="utf-8") as infile, open(f"unique_{file_name}", "w", encoding="utf-8") as outfile:
        for line in infile:
            if line not in res:
                res.append(line)
        outfile.writelines(res)
    print(f"Дубликаты удалены. Уникальные строки сохранены в unique_{file_name}")
