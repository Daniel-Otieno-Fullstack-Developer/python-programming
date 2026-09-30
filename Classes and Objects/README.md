# Python Classes and Objects

Eight intermediate tasks on object-oriented programming: classes, `__init__`, methods, encapsulation, `__str__`, class attributes and inheritance.

## Tasks

| File | Task | Covers | What it does |
|---|---|---|---|
| [task1.py](task1.py) | First Student Class | `class`, `__init__` | Creates two student objects and introduces them |
| [task2.py](task2.py) | Rectangle | methods | Rectangle methods for area, perimeter and tiles |
| [task3.py](task3.py) | Bank Account | encapsulation | An account that checks deposits and withdrawals |
| [task4.py](task4.py) | Marks With Validation | getters, setters | Validates marks with a setter and grades them |
| [task5.py](task5.py) | Gate Counter | class attribute, `__str__` | Counts people in and out with a class attribute |
| [task6.py](task6.py) | Shop Stock | list of objects | Totals stock value from a list of objects |
| [task7.py](task7.py) | Person and Student | inheritance, `super()` | Student and Lecturer inherit from Person |
| [task8.py](task8.py) | Library System | objects together | A library that lends and returns books |

## Sample output

**Task 3: Bank Account**
```
Account holder: Wanjiku Mwangi
Opening balance (KES): 5000
Deposit (KES): 2500
  Deposited KES 2,500.00
Withdraw (KES): 10000
  Refused: balance is only KES 7,500.00
Withdraw (KES): 3200
  Withdrew KES 3,200.00
Wanjiku Mwangi's balance: KES 4,300.00
```

**Task 8: Library System**
```
Omar Farah borrowed 'Python Crash Course'.
'Python Crash Course' is already out with Omar Farah.
No such book.
'Python Crash Course' is back on the shelf.
Mercy Achieng borrowed 'Web Design with HTML'.
Library report:
  B1  Python Crash Course       available
  B2  Networking Essentials     available
  B3  Web Design with HTML      out: Mercy Achieng
```

## Run a task

```bash
python task1.py
```

On Windows you can also use `py task1.py`; on Linux and macOS use `python3 task1.py`.
