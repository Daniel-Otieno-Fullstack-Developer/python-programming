# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Dictionaries and Sets Assignment
# Task 7: Club Members
# Run with: python task7.py

# Sets hold each name once, in no particular order
coding_club = {"Amina", "Brian", "Chebet", "Dahir", "Esther"}
football = {"Brian", "Dahir", "Farah", "Grace"}

print("Coding club:", sorted(coding_club))
print("Football:   ", sorted(football))
print("In both:          ", sorted(coding_club & football))
print("In either:        ", sorted(coding_club | football))
print("Coding only:      ", sorted(coding_club - football))
print("Only one of them: ", sorted(coding_club ^ football))

name = input("Who wants to join coding club? ").strip().title()
if name in coding_club:
    print(name, "is already a member.")
else:
    coding_club.add(name)
    print(name, "added. Members now:", len(coding_club))
