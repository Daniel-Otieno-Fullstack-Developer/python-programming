# Python Strings

Eight beginner tasks on working with text: indexing and slicing strings, string methods, `find()`, `split()` and `join()`, and f-string formatting.

## Tasks

| File | Task | Covers | What it does |
|---|---|---|---|
| [task1.py](task1.py) | Name Formatter | `strip()`, `title()`, `split()` | Cleans a name and prints its case forms and initials |
| [task2.py](task2.py) | Username Generator | slicing, `lower()` | Builds a username and email from name and year |
| [task3.py](task3.py) | Letter Counter | loop, `isalpha()`, `isdigit()` | Counts letters, digits and spaces in a sentence |
| [task4.py](task4.py) | Palindrome Checker | `[::-1]`, `isalnum()` | Checks whether text reads the same backwards |
| [task5.py](task5.py) | M-Pesa Message Reader | `find()`, slices | Extracts details from an M-Pesa style SMS |
| [task6.py](task6.py) | Word Tools | `split()`, `join()` | Splits, reverses, joins and counts words |
| [task7.py](task7.py) | Password Strength | `isupper()`, `isdigit()` | Tests a password against four rules until it passes |
| [task8.py](task8.py) | Receipt Printer | f-string widths | Prints an aligned receipt with VAT |

## Sample output

**Task 5: M-Pesa Message Reader**
```
Transaction code: QJK7TX2L9P
Amount sent:      KES 1,250.00
Sent to:          Amina Yusuf
Balance left:     KES 3,480.50
```

**Task 8: Receipt Printer**
```
==================================
      DELHI COLLEGE BOOKSHOP      
        Eastleigh, Nairobi        
==================================
Exercise books x10          650.00
Biro pens x5                100.00
Geometry set                380.00
Scientific calculator     1,850.00
----------------------------------
TOTAL                     2,980.00
Includes VAT (16%)          411.03
==================================
           Asante sana!           
```

## Run a task

```bash
python task1.py
```

On Windows you can also use `py task1.py`; on Linux and macOS use `python3 task1.py`.
