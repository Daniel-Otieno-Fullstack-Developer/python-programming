# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 3: Letter Counter
# Run with: python task3.py

sentence = input("Type a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Characters:", len(sentence))
print("Vowels:    ", vowels)
print("Consonants:", consonants)
print("Digits:    ", digits)
print("Spaces:    ", spaces)
print("Words:     ", len(sentence.split()))
