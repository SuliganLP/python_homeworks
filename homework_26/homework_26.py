# Список файлов и папок
# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
# ● Отдельно список папок
# ● Отдельно список файлов
# Пример запуска:
# python script.py /home/user/documents
# Пример вывода:
# Содержимое директории '/home/user/documents':
# Папки:
# - folder1
# - folder2
# Файлы:
# - file1.txt
# - file2.txt
# - notes.docx

import os
import sys

if len(sys.argv) != 2:
    print("Использование: python script.py <директория>")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"Директория {directory} не существует")
    sys.exit(1)

folders = []
files = []

for item in os.listdir(directory):
    full_path = os.path.join(directory, item)
    if os.path.isdir(full_path):
        folders.append(item)
    elif os.path.isfile(full_path):
        files.append(item)

print(f"Содержимое директории: {directory}")

print(f"Папки: ")
for elem in folders:
    print(f"- {elem}")

print(f"Файлы: ")
for elem in files:
    print(f"- {elem}")


# Поиск и удаление файлов с указанным расширением
# Напишите программу, которая
# ● Принимает путь к директории и расширение файлов через аргумент командной строки.
# ● Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
# ● Спрашивает у пользователя, хочет ли он удалить найденные файлы.
# ● Если пользователь подтверждает, удаляет их.
# Пример запуска
# python script.py /home/user/PycharmProjects/project1 .log
# Пример вывода:
# Найдены файлы с расширением '.log':
# - logs/error.log
# - logs/system.log
# - logs/backup/old.log
# - logs/backup/debug.log
# Вы хотите удалить эти файлы? (y/n): y
# Удаление завершено.


import os
import sys

if len(sys.argv) != 3:
    print("Использование: python script.py <директория> <расширение>")
    sys.exit(1)

directory = sys.argv[1]
extension = sys.argv[2]

if not os.path.isdir(directory):
    print(f"Директория {directory} не существует")
    sys.exit(1)

found_files = []

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(extension):
            full_path = os.path.join(root, file)
            found_files.append(full_path)

if not found_files:
    print(f"Файлы с расширением '{extension}' не найдены")
    sys.exit(0)

print(f"Найдены файлы с расширением {extension}")

for elem in found_files:
    print(f"- {elem}")

to_delete = input("Вы хотите удалить эти файлы? (y/n): ")

if to_delete == "y":
    for item in found_files:
        os.remove(item)
    print("Удаление завершено")

elif to_delete == "n":
    print("Завершено без удаления файлов")

else:
    print("Некорректная команда")
