# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 2: Save a Class List
# Run with: python task2.py

class_name = input("Class name: ")
count = int(input("How many students? "))

# "w" creates the file, or empties it if it already exists
with open("class_list.txt", "w") as file:
    file.write(f"CLASS LIST - {class_name}\n")
    for number in range(1, count + 1):
        name = input(f"Student {number}: ")
        file.write(f"{number}. {name}\n")

print("Saved", count, "names to class_list.txt")

# Read the file back to check what was written
print()
with open("class_list.txt", "r") as file:
    print(file.read(), end="")
