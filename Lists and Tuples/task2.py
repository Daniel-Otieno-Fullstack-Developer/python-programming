# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 2: Weekly Sales Report
# Run with: python task2.py

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
sales = []                                 # start with an empty list

for day in days:
    amount = float(input(f"Sales on {day} (KES): "))
    sales.append(amount)                   # add it to the end of the list

total = sum(sales)
best = max(sales)
best_day = days[sales.index(best)]         # same position in both lists

print()
print(f"Total sales:   KES {total:,.2f}")
print(f"Average a day: KES {total / len(sales):,.2f}")
print(f"Best day:      {best_day} (KES {best:,.2f})")
print(f"Worst day:     {days[sales.index(min(sales))]} (KES {min(sales):,.2f})")
