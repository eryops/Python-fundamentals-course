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

# account1 = BankAccount('Johanna', 1000)
# print(account1)
# account1.deposit(200)
# print(account1)
# account1.withdraw(2000)

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

    def __repr__(self):
        return f'Task(title={self.title}, completed={self.completed})'

task_one = Task('Clean dishes')
task_two = Task('Clean bathroom')

task_one.complete()
print(task_one)
print(task_two)
        
        