# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 6: Word Tools
# Run with: python task6.py

sentence = input("Type a sentence: ")

words = sentence.split()            # split on spaces into a list of words
print("Number of words:", len(words))

longest = ""
hashtag = "#"
for word in words:
    if len(word) > len(longest):
        longest = word
    hashtag += word.capitalize()

print("Longest word:   ", longest)
print("Reversed order: ", " ".join(words[::-1]))
print("Joined with -:  ", "-".join(words))
print("Hashtag:        ", hashtag)

# Count how many times a chosen word appears
target = input("Word to count: ").lower()
times = sentence.lower().split().count(target)
print(f"'{target}' appears {times} time(s)")
