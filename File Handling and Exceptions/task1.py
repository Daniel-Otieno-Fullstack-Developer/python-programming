# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 1: Notice Board Reader
# Run with: python task1.py

# Uses the sample file notices.txt in this folder
line_count = 0
word_count = 0

with open("notices.txt", "r") as file:
    for line in file:
        line = line.strip()              # remove the newline at the end
        line_count += 1
        word_count += len(line.split())
        print(f"{line_count}. {line}")

print()
print("Lines:", line_count)
print("Words:", word_count)
