class BankAccount:
    def __init__(self, balance):
        self.balance = balance


bank = BankAccount(1000)

print(bank.balance)
bank.balance = 10000000
print(bank.balance)
