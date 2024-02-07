class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено: {amount}. Баланс: {self.balance}")
        else:
            print("Сумма внесения должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снято: {amount}. Баланс: {self.balance}")
        else:
            print("Недостаточно средств на балансе")

    def __str__(self):
        return f"Владелец: {self.owner}\n Баланс: {self.balance}"
    
Amir = Account("Amir", 10000)
Amir.deposit(10000)
Amir.withdraw(30000)
Amir.withdraw(15000)
Amir.deposit(5000)