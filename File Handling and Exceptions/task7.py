# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - File Handling and Exceptions Assignment
# Task 7: Open Any File
# Run with: python task7.py

while True:
    filename = input("File to open (or Q to quit): ")
    if filename.upper() == "Q":
        break
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"  Cannot find '{filename}'. Check the name and try again.")
    else:
        # runs only when open() worked
        lines = file.readlines()
        file.close()
        print(f"  {filename} has {len(lines)} lines. First line:")
        print("  " + lines[0].strip())
    finally:
        print("  -- done with this attempt --")
