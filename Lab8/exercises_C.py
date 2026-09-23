class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance or 0

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate or 0

account1 = SavingsAccount("Johanna", 1500, 0.02)
account2 = SavingsAccount("Alex", 3000, 0.015)

print(account1.owner, account1.balance, account1.interest_rate)
print(account2.owner, account2.balance, account2.interest_rate)