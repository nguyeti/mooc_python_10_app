class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            # create an instance variable balance self is the current object like "this" in java
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# Inheritance Checking extends Account
class Checking(Account):
    """ this is a doc string"""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
# account=Account("balance.txt")
# print("balance is " + str(account.balance))
# account.withdraw(350)
# print("balance is " + str(account.balance))
# account.deposit(5500)
# print("balance is " + str(account.balance))
# account.commit()

checking1 = Checking("balance.txt", 1)
checking1.transfer(5460)
checking1.commit()
print(checking1.__doc__)
