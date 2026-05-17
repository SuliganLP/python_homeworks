# Банковский счёт
# создайте класс BankAccount, описывающий
# банковский счёт.
# ● Объект должен хранить имя владельца и
# текущий баланс.
# ● Реализуйте методы:
# ○ пополнение счёта
# ○ снятие средств
# ○ отображение баланса
# ● При попытке снять больше, чем есть на счёте,
# операция не должна выполняться.
# Продумайте, какие поля и методы следует скрыть от
# внешнего доступа, а какие оставить открытыми.
# Пример вывода:
# Current balance: 150
# Error: Amount must be positive.
# Current balance: 150
# Error: Not enough funds.
# Current balance: 150

# История операций
# доработайте класс BankAccount.
# ● Каждая операция пополнения и снятия должна сохраняться в историю.
# ● История должна быть доступна через property history только для чтения.
# ● История представляется в виде списка строк ("Deposit: 150", "Withdraw:
# 100" и т.д.).
# Пример вывода:
# Current balance: 50
# Operation history:
# Deposit: 150
# Withdraw: 100

class BankAccount:
    def __init__(self, name: str, balance: int | float = 150) -> None:
        self.name = name
        self._balance = balance
        self._history = []

    def show_balance(self) -> str:
        return f"Current balance: {self._balance}"

    def deposit(self, amount: int | float) -> str:
        if not isinstance(amount, int | float):
            raise TypeError("Amount should be int or float")
        if amount <= 0:
            raise ValueError("Error: Amount must be positive.")

        self._balance += amount
        self._history.append(f"Deposit: {amount}")

        return self.show_balance()

    def withdraw(self, amount: int | float) -> str:
        if not isinstance(amount, int | float):
            raise TypeError("Amount should be int or float")
        if amount <= 0:
            raise ValueError("Error: Amount must be positive.")
        if amount > self._balance:
            return "Error: Not enough funds."

        self._balance -= amount
        self._history.append(f"Withdraw: {amount}")

        return self.show_balance()

    @property
    def history(self) -> list[str]:
        return self._history.copy()


account = BankAccount("Alex")


print(account.show_balance())
print(account.deposit(-50))
print(account.show_balance())
print(account.withdraw(200))
print(account.show_balance())
print(account.deposit(100))
print(account.withdraw(150))

print("Operation history:")
for operation in account.history:
    print(operation)
