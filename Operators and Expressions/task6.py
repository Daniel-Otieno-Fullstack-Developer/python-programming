# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 6: CAT Average
# Run with: python task6.py

PASS_MARK = 50

cat1 = int(input("CAT 1 mark: "))
cat2 = int(input("CAT 2 mark: "))
cat3 = int(input("CAT 3 mark: "))

total = cat1 + cat2 + cat3
# Brackets make Python add first, then divide
average = (cat1 + cat2 + cat3) / 3
passed = average >= PASS_MARK

print("Total:  ", total)
print("Average:", round(average, 1))
print("Passed: ", passed)
