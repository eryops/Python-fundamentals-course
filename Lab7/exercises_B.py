class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        raise ValueError('You are to poor to do that')

    def __repr__(self):
        return f'Bank account (owner = {self.owner}, balance = {self.balance})'

account1 = BankAccount('Johanna', 1000)
print(account1)
account1.deposit(200)
print(account1)
account1.withdraw(2000)
        