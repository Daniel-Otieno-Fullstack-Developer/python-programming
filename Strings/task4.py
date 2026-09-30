# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 4: Palindrome Checker
# Run with: python task4.py

def is_palindrome(text):
    """Return True if text reads the same backwards (ignoring case and spaces)."""
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum():
            cleaned += ch
    return cleaned == cleaned[::-1]


for attempt in range(3):
    word = input("Word or phrase: ")
    if is_palindrome(word):
        print(f'"{word}" is a palindrome.')
    else:
        print(f'"{word}" is not a palindrome.')
