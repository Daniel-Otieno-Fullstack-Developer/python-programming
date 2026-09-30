# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 4: Word Frequency
# Run with: python task4.py

text = input("Paste a sentence: ").lower()

counts = {}
for word in text.split():
    word = word.strip(".,!?;:")        # remove punctuation at the ends
    if word == "":
        continue
    counts[word] = counts.get(word, 0) + 1

print("Different words:", len(counts))
for word in sorted(counts):
    print(f"{word:<10} {'*' * counts[word]} ({counts[word]})")
