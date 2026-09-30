# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 1: Welcome Banner
# Run with: python task1.py

def print_banner(title, width):
    """Print title centred between two lines of = signs."""
    print("=" * width)
    print(title.center(width))
    print("=" * width)


course = input("Course name: ")
print_banner("DELHI COLLEGE", 30)
print_banner(course, 30)
