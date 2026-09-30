# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Lists and Tuples Assignment
# Task 3: Shopping List
# Run with: python task3.py

shopping = ["maize flour", "sugar", "milk"]
print("Start:", shopping)

shopping.append("bread")               # add to the end
shopping.insert(0, "cooking oil")      # add at position 0
print("After adding:", shopping)

item = input("Which item did you already buy? ")
if item in shopping:
    shopping.remove(item)
    print(f"Removed {item}.")
else:
    print(f"{item} is not on the list.")

last = shopping.pop()                  # take the last item off
print("Took off the last item:", last)

shopping.sort()
print("Sorted list:", shopping)
print("Items left:", len(shopping))
