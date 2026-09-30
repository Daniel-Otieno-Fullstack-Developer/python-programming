# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 2: Username Generator
# Run with: python task2.py

first = input("First name: ").strip().lower()
last = input("Last name: ").strip().lower()
year = input("Year of admission: ").strip()

# first three letters of the first name + surname + last two digits of the year
username = first[:3] + last + year[-2:]
email = f"{username}@delhicollege.co.ke"

print("Username:", username)
print("Email:   ", email)
