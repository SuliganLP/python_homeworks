# Электронное письмо
# Реализуйте класс Email, который представляет электронное письмо. Каждое письмо должно содержать:
#
# sender — адрес отправителя
# recipient — адрес получателя
# subject — тема письма
# body — текст письма
# date — дата отправки

# Класс должен поддерживать:
#
# Сравнение писем по дате
# Преобразование письма в строку
# Получение длины текста письма
# Проверку на наличие текста в письме или не состоит ли текст только из пробелов
#
# Пример использования:
#
# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e1)
# print(e2)
# print("Length:", len(e1))
# print("Has text:", bool(e1))
# print("Is newer:", e2 > e1)
# Пример вывода:
#
# From: alice@example.com
# To: bob@example.com
# Subject: Meeting
# - Let's meet at 10am -
# From: bob@example.com
# From: bob@example.com
# To: alice@example.com
# Subject: Report
# -  -
# Length: 18
# Length: 18
# Has text: True
# Is newer: True

from datetime import datetime
from functools import total_ordering


@total_ordering
class Email:
    def __init__(self, sender: str, recipient: str, subject: str, body: str, date: datetime) -> None:
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self) -> str:
        return (f"From: {self.sender}\n"
                f"To: {self.recipient}\n"
                f"Subject: {self.subject}\n"
                f"- {self.body} -")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Email):
            return NotImplemented
        return self.date == other.date

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Email):
            return NotImplemented
        return self.date > other.date

    def __len__(self) -> int:
        return len(self.body)

    def __bool__(self) -> bool:
        return bool(self.body.strip())


e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

# Создайте класс Money, в котором можно:
# складывать и вычитать объекты через операторы + и -
# выводить объект как строку в виде "$<amount>"
# при сложении и вычитании возвращается новый объект
# если вычитание приводит к отрицательному значению — вернуть 0
#
# Пример использования:
# money1 = Money(100)
# money2 = Money(50)
# print(money1 + money2)
# print(money1 + money2)
# print(money1 - money2)
# print(money2 - money1)
# Пример вывода:
#
# $150
# $50
# $0


class Money:
    def __init__(self, amount: int | float) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return f"${self.amount}"

    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __sub__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented

        result = self.amount - other.amount

        if result < 0:
            result = 0

        return Money(result)


money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)
