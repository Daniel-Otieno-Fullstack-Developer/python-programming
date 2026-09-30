# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 3: Change Machine
# Run with: python task3.py

change = int(input("Change to give (KES): "))

# Work from the largest note down. // counts how many fit,
# % keeps what is still left to give.
thousands = change // 1000
change = change % 1000
five_hundreds = change // 500
change = change % 500
two_hundreds = change // 200
change = change % 200
hundreds = change // 100
change = change % 100
fifties = change // 50
change = change % 50
twenties = change // 20
change = change % 20
tens = change // 10
change = change % 10
fives = change // 5
ones = change % 5

print("1000 notes:", thousands)
print(" 500 notes:", five_hundreds)
print(" 200 notes:", two_hundreds)
print(" 100 notes:", hundreds)
print("  50 notes:", fifties)
print("  20 coins:", twenties)
print("  10 coins:", tens)
print("   5 coins:", fives)
print("   1 coins:", ones)
