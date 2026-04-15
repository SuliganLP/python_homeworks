"""
Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы,
игнорируя регистр.
Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""
from collections import defaultdict
from collections import Counter

text = "Programming is fun!"

char_counter = Counter(char for char in text.lower() if char.isalpha())
print(dict(char_counter))

"""
Группировка студентов по классам
Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3",
"Daisy")]
Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
"""
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

dd = defaultdict(list)

for class_name, student in students:
    dd[class_name].append(student)

print(dict(dd))
