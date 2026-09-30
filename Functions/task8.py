# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 8: Loan Repayment
# Run with: python task8.py

def monthly_payment(amount, yearly_rate, months):
    """Return the fixed monthly repayment for a loan (reducing balance)."""
    r = yearly_rate / 100 / 12
    if r == 0:
        return amount / months
    return amount * r / (1 - (1 + r) ** -months)


def print_summary(amount, yearly_rate, months):
    payment = monthly_payment(amount, yearly_rate, months)
    total = payment * months
    print(f"Monthly payment: KES {payment:,.2f}")
    print(f"Total repaid:    KES {total:,.2f}")
    print(f"Total interest:  KES {total - amount:,.2f}")


loan = float(input("Loan amount (KES): "))
rate = float(input("Interest rate per year (%): "))
months = int(input("Months to repay: "))
print_summary(loan, rate, months)
