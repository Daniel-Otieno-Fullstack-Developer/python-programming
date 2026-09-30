# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 8: M-Pesa Statement
# Run with: python task8.py

import csv

# Uses mpesa_statement.csv. Some rows have a missing or bad amount;
# the program reports them instead of crashing.
money_in = 0.0
money_out = 0.0
bad_rows = 0

with open("mpesa_statement.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)                        # skip the heading row
    for line_number, row in enumerate(reader, start=2):
        date, details, kind, amount_text = row
        try:
            amount = float(amount_text)
        except ValueError:
            print(f"Line {line_number}: bad amount '{amount_text}'")
            bad_rows += 1
            continue
        if kind == "in":
            money_in += amount
        else:
            money_out += amount

print()
print(f"Money in:   KES {money_in:>10,.2f}")
print(f"Money out:  KES {money_out:>10,.2f}")
print(f"Net change: KES {money_in - money_out:>10,.2f}")
print("Rows skipped:", bad_rows)
