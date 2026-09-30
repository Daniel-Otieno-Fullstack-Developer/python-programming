# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 3: Bank Account
# Run with: python task3.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance          # leading _ means "use the methods"

    def deposit(self, amount):
        if amount <= 0:
            print("  Deposit must be more than zero.")
            return
        self._balance += amount
        print(f"  Deposited KES {amount:,.2f}")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"  Refused: balance is only KES {self._balance:,.2f}")
            return
        self._balance -= amount
        print(f"  Withdrew KES {amount:,.2f}")

    def get_balance(self):
        return self._balance


owner = input("Account holder: ")
opening = float(input("Opening balance (KES): "))
account = BankAccount(owner, opening)

account.deposit(float(input("Deposit (KES): ")))
account.withdraw(float(input("Withdraw (KES): ")))
account.withdraw(float(input("Withdraw (KES): ")))
print(f"{account.owner}'s balance: KES {account.get_balance():,.2f}")
