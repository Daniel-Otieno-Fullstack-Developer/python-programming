# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 4: Class Average
# Run with: python task4.py

total = 0
count = 0

mark = int(input("Enter a mark (-1 to finish): "))

# -1 is the sentinel: the signal to stop
while mark != -1:
    total += mark
    count += 1
    mark = int(input("Enter a mark (-1 to finish): "))

if count > 0:
    print("Marks entered:", count)
    print("Total:", total)
    print("Average:", round(total / count, 1))
else:
    print("No marks entered.")
