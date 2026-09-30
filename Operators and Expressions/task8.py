# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Operators and Expressions Assignment
# Task 8: Exam Eligibility
# Run with: python task8.py

MIN_ATTENDANCE = 75

fee_balance = float(input("Fee balance (KES): "))
attendance = float(input("Attendance (%): "))

fees_cleared = fee_balance == 0
attended_enough = attendance >= MIN_ATTENDANCE

# and: both must be True. or: at least one True. not: flips the value.
eligible = fees_cleared and attended_enough
needs_follow_up = not fees_cleared or attendance < 50

print("Fees cleared:    ", fees_cleared)
print("Attendance OK:   ", attended_enough)
print("Can sit the exam:", eligible)
print("Needs follow-up: ", needs_follow_up)
