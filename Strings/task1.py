# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 1: Name Formatter
# Run with: python task1.py

full_name = input("Enter your full name: ")

# split() drops all extra spaces, join() puts one space back between words,
# and title() gives each word a capital letter
clean = " ".join(full_name.split()).title()

print("Cleaned:    ", clean)
print("Upper case: ", clean.upper())
print("Lower case: ", clean.lower())
print("Letters:    ", len(clean.replace(" ", "")))
print("Initials:   ", end=" ")
for word in clean.split():
    print(word[0] + ".", end="")
print()
