# Счётчик экземпляров
# Создайте класс User, представляющий пользователя.
# ● При создании должны указываться логин (username) и пароль (password).
# ● У класса должно быть поле total_users, хранящее общее количество
# созданных пользователей.
# ● При каждом создании нового объекта User, счётчик должен увеличиваться.
# ● Добавьте метод get_total(), возвращающий количество пользователей.
# ● Проверьте, что счётчик работает.
# Пример вывода:
# Total users: 2

class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users


user_1 = User("Alex", "12345")
user_2 = User("John", "12345")

print(f"Total users: {User.get_total()}")


# Проверка данных пользователя
# Доработайте класс User.
# ● Добавьте валидации полей при создании.
# ● Имя должно быть непустой строкой.
# ● Пароль должен быть строкой длиной не менее 5 символов.
# ● Если данные некорректны — выбрасывайте ValueError.
# ● Добавьте строковое представление объекта.
# ● Проверьте работу класса с разными значениями.
# Пример вывода:
# User: alice
#  ...
# ValueError: Invalid password:
# 'qwe'.
# Пример вызова:
# user1 = User("alice", "secret")
# user2 = User("bob", "qwe")


class User:
    total_users = 0

    def __init__(self, username, password):
        if not isinstance(username, str) or username.strip() == "":
            raise ValueError("Invalid username")

        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f"Invalid password: '{password}'")

        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

    def __str__(self):
        return f"User: {self.username}"
