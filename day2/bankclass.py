class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{self.name}: Deposited {amount}. New balance is {self.balance}"
        else:
            return "Error! Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return f"{self.name}: Insufficient balance! Current balance is {self.balance}"
        elif amount <= 0:
            return "Error! Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"{self.name}: Withdrawn {amount}. Remaining balance is {self.balance}"



account1 = BankAccount("Alice", 5000)
account2 = BankAccount("Bob", 10000)


print(account1.deposit(2000))
print(account1.withdraw(1500))

print(account2.deposit(500))
print(account2.withdraw(12000))
