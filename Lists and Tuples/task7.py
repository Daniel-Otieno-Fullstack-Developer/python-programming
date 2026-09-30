# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 7: Matatu Stages
# Run with: python task7.py

# Each stage is a tuple: (name, fare from town). Tuples cannot be changed.
stages = [
    ("Eastleigh", 50),
    ("Pangani", 60),
    ("Muthaiga", 80),
    ("Kasarani", 100),
    ("Ruiru", 120),
]

print("STAGE          FARE")
for name, fare in stages:                  # unpack each tuple
    print(f"{name:<14} KES {fare}")

stop = input("Where are you going? ")
found = False
for name, fare in stages:
    if name == stop:
        print(f"The fare to {name} is KES {fare}.")
        found = True
        break

if not found:
    print("That stage is not on this route.")
