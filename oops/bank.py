#Classes and Objects :

class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Calling/Accessing a class
a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(b.deposit(50))
print(b.withdraw(10))
print(a.withdraw(10))

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

x=MinimumBalanceAccount()
y=MinimumBalanceAccount()

print(x(10))
print(y(20))