# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Data Types and Variables Assignment
# Task 5: Temperature Converter
# Run with: python task5.py

celsius = float(input("Temperature in Nairobi (Celsius): "))

# Formula: F = C x 9 / 5 + 32
fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius} Celsius is {fahrenheit:.1f} Fahrenheit")
