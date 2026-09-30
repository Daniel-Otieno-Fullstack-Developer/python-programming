# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 6: Fee Balance Report
# Run with: python task6.py

import csv

# Read fees.csv and write the students who still owe money to fee_report.txt
owing = []
with open("fees.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        balance = int(row["fees"]) - int(row["paid"])
        if balance > 0:
            owing.append((row["adm_no"], row["name"], balance))

total_owed = 0
with open("fee_report.txt", "w") as report:
    report.write("FEE BALANCE REPORT - DELHI COLLEGE\n")
    for adm, name, balance in owing:
        report.write(f"{adm}  {name:<16} KES {balance:>7,}\n")
        total_owed += balance
    report.write(f"Students owing: {len(owing)}\n")
    report.write(f"Total owed: KES {total_owed:,}\n")

print(f"Report saved to fee_report.txt ({len(owing)} students owing).")
