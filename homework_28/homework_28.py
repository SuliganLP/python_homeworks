# Фильтрация по ключевому слову
# напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на
# следующий день недели, пока пользователь нажимает 'Enter'.
# Пример ввода:
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана:
# Tuesday: Meeting, Work, Study Python
# ...
# Нажмите 'Enter' для получения плана:
# Sunday: Family time, Rest
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана: q
# Данные:
# # Расписание дел на неделю
import itertools

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]}

weekly_generator = itertools.cycle(weekly_schedule.items())

while True:

    user_input = input("Нажмите 'Enter' для получения плана или напечатайте 'q' для выхода: ")

    if user_input == "":
        day, tasks = next(weekly_generator)
        print(f"{day}: {', '.join(tasks)}")
    elif user_input == "q":
        print("Программа завершена")
        break


# Объединение списков продуктов
# напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
# содержащий все продукты в нижнем регистре. Выведите содержимое генератора.
# Пример вывода:
# apple
# banana
# orange
# carrot
# tomato
# cucumber
# milk
# cheese
# yogurt
# Данные:


fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def merge_products(*product_lists):
    return (product.lower() for product in itertools.chain(*product_lists))


products_generator = merge_products(fruits, vegetables, dairy)

for product_name in products_generator:
    print(product_name)


# Комбинации одежды
# Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все
# возможные комбинации в формате "Clothe - Color - Size".
# Пример вывода:
# T-shirt - Red - S
# T-shirt - Red - M
# T-shirt - Red - L
# T-shirt - Blue - S
# ...
# Jacket - Black - L
# Данные:

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def clothes_combination(clothes, colors, sizes):
    return (f"{clothe} - {color} - {size}" for clothe, color, size in itertools.product(clothes, colors, sizes))


combination_generator = clothes_combination(clothes, colors, sizes)

for comb in combination_generator:
    print(comb)
