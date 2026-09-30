# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 7: Password Strength
# Run with: python task7.py

def check_password(password):
    """Return a list of the rules the password breaks."""
    problems = []
    if len(password) < 8:
        problems.append("at least 8 characters")
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    if not has_upper:
        problems.append("a capital letter")
    if not has_lower:
        problems.append("a small letter")
    if not has_digit:
        problems.append("a digit")
    return problems


while True:
    password = input("Choose a password: ")
    missing = check_password(password)
    if not missing:
        print("Strong password. Account created.")
        break
    print("Weak. It needs " + ", ".join(missing) + ".")
