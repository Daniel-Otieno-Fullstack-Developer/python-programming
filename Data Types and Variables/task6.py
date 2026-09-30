# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Data Types and Variables Assignment
# Task 6: Type Detective
# Run with: python task6.py

text = input("Type a whole number: ")
print("You typed", text, "and its type is", type(text))

# The same value converted to three other types
as_int = int(text)
as_float = float(text)
as_bool = bool(as_int)     # 0 becomes False, any other number becomes True

print("As an int:  ", as_int, type(as_int))
print("As a float: ", as_float, type(as_float))
print("As a bool:  ", as_bool, type(as_bool))
print("Doubled as int:", as_int * 2, "| doubled as text:", text * 2)
