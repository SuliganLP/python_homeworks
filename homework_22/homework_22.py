# Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену. Напишите функцию, которая:
# 1. Отбирает заказы дороже 500.
# 2. Создаёт список названий отобранных продуктов в алфавитном порядке.
# 3. Возвращает итоговый список названий.

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]


def select_products(orders: list[dict], min_price: int = 500) -> list[str]:
    expensive_orders = filter(lambda order: order["price"] > min_price, orders)

    product_names = map(lambda order: order["product"], expensive_orders)

    return sorted(product_names)

# Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
# 1. Вычисляет общую выручку для каждого товара.
# 2. Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000,
# 'Monitor': 3000, 'Keyboard': 1500,
# 'Mouse': 1000}


sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

res_dict = {}
for product, quantity, price in sales:
    revenue = quantity * price
    res_dict[product] = res_dict.get(product, 0) + revenue

print(dict(sorted(res_dict.items(), key=lambda x: x[1], reverse=True)))
