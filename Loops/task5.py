# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Loops Assignment
# Task 5: PIN Check
# Run with: python task5.py

CORRECT_PIN = "2580"
MAX_ATTEMPTS = 3

unlocked = False
for attempt in range(1, MAX_ATTEMPTS + 1):
    pin = input(f"Attempt {attempt} - enter PIN: ")
    if pin == CORRECT_PIN:
        unlocked = True
        break                         # stop asking once the PIN is right
    print("Wrong PIN.", MAX_ATTEMPTS - attempt, "attempt(s) left.")

if unlocked:
    print("PIN accepted. Welcome.")
else:
    print("Card blocked. Visit your nearest branch.")
