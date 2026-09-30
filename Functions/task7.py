# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 7: Scope Explorer
# Run with: python task7.py

college = "Delhi College"        # global: can be read anywhere
visitors = 0                     # global counter


def show_scope():
    room = "Lab 3"               # local: exists only inside this function
    print("Inside the function:", college, "-", room)


def sign_in(name):
    global visitors              # we want to change the global variable
    visitors += 1
    print(f"{name} signed in. Visitors today: {visitors}")


show_scope()
print("Outside the function:", college)

for person in range(3):
    sign_in(input("Visitor name: "))

print("Final count:", visitors)
