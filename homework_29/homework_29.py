# Создайте генератор, который генерирует последовательность Фибоначчи бесконечно,
# возвращая по одному числу за раз.
#
# Последовательность Фибоначчи — это ряд чисел, где каждое следующее число равно сумме двух предыдущих.
# Начинается с 0 и 1.
#
# Пример вывода:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fib_gen():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


gen = fib_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Генератор уникальных элементов
# создайте генератор, который принимает список элементов и выдаёт только уникальные значения, сохраняя
# порядок их появления в исходном списке
# Пример вывода:
# 3
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# Данные:

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


def generator(items):
    used_nums = set()

    for num in items:
        if num not in used_nums:
            used_nums.add(num)
            yield num


for elem in generator(data):
    print(elem)
