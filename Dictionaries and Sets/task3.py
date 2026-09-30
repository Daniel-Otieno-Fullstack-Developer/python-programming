# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 3: Phone Book
# Run with: python task3.py

contacts = {}

while True:
    print("1. Add or update  2. Find  3. Delete  4. Show all  5. Quit")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ").title()
        contacts[name] = input("Phone: ")
        print("Saved.")
    elif choice == "2":
        name = input("Name: ").title()
        print(contacts.get(name, "Not found"))
    elif choice == "3":
        name = input("Name: ").title()
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Not found")
    elif choice == "4":
        for name in sorted(contacts):
            print(f"{name:<15} {contacts[name]}")
    elif choice == "5":
        print("Goodbye.")
        break
    else:
        print("Please choose 1 to 5.")
