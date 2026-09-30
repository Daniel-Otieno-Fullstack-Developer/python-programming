# Python Loops

Eight beginner tasks on repeating code with `for` and `range()`, `while` loops with sentinels, `break` and `continue`, and nested loops.

## Tasks

| File | Task | Covers | What it does |
|---|---|---|---|
| [task1.py](task1.py) | Countdown | `for`, `range()` steps | Counts down, then lists even numbers with `range()` steps |
| [task2.py](task2.py) | Times Table | `for`, `range()` | Prints a 12-line times table |
| [task3.py](task3.py) | Weekly Sales | running total | Reads each day's sales and totals them |
| [task4.py](task4.py) | Class Average | `while` + sentinel | Totals marks until the -1 sentinel |
| [task5.py](task5.py) | PIN Check | `for` + `break` | Three PIN attempts, stopping early with `break` |
| [task6.py](task6.py) | Savings Goal | `while` | Repeats weekly savings until a goal is met |
| [task7.py](task7.py) | Even Numbers Only | `continue` | Skips odd numbers with `continue` and sums the rest |
| [task8.py](task8.py) | Multiplication Grid | nested `for` | Builds a multiplication grid with nested loops |

## Sample output

**Task 5: PIN Check**
```
Attempt 1 - enter PIN: 1234
Wrong PIN. 2 attempt(s) left.
Attempt 2 - enter PIN: 0000
Wrong PIN. 1 attempt(s) left.
Attempt 3 - enter PIN: 2580
PIN accepted. Welcome.
```

**Task 8: Multiplication Grid**
```
Grid size: 6
   |   1   2   3   4   5   6
---+------------------------
 1 |   1   2   3   4   5   6
 2 |   2   4   6   8  10  12
 3 |   3   6   9  12  15  18
 4 |   4   8  12  16  20  24
 5 |   5  10  15  20  25  30
 6 |   6  12  18  24  30  36
```

## Run a task

```bash
python task1.py
```

On Windows you can also use `py task1.py`; on Linux and macOS use `python3 task1.py`.
