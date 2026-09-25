class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account(owner={self.owner}, balance={self.balance})"

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return (f"SavingsAccount(owner={self.owner}, "
                f"balance={self.balance}, interest_rate={self.interest_rate})")

acc = Account("Johanna", 1200)
sacc = SavingsAccount("Johanna", 1500, 0.02)

print(acc)
print(sacc)
