import random


class Account:
    def __init__(self, owner: str, balance: int):
        self._account_id = random.randint(1, 25)
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self._balance += amount
        return "Счет пополнен"

    def withdraw(self, amount: int):
        if amount > 0 and self._balance > amount:
            self._balance -= amount
        return "Деньги сняты со счета"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, (float, int)) and value > 0:
            self._balance = value

    def __str__(self):
        return f"Account id - {self._account_id}, владелец - {self.owner}, баланс - {self._balance}"


acc1 = Account("Stepa", 15000)
print(acc1)
print(acc1.balance)
