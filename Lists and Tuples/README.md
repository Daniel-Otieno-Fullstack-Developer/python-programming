# Python Lists and Tuples

Eight beginner tasks on lists and tuples: indexing, slicing, list methods, totals, searching, sorting (including a bubble sort) and a list of lists.

## Tasks

| File | Task | Covers | What it does |
|---|---|---|---|
| [task1.py](task1.py) | Class List | indexing, slicing | Reads items by index and slice, then numbers them |
| [task2.py](task2.py) | Weekly Sales Report | `append()`, `max()`, `index()` | Builds a sales list and finds the best and worst day |
| [task3.py](task3.py) | Shopping List | list methods | Uses `append`, `insert`, `remove`, `pop` and `sort` |
| [task4.py](task4.py) | Search the Register | linear search | Searches a list with a loop and with `index()` |
| [task5.py](task5.py) | Top Marks | `sorted()`, slices | Sorts marks highest first and slices the top three |
| [task6.py](task6.py) | Bubble Sort | bubble sort | Bubble sorts a list and counts the swaps |
| [task7.py](task7.py) | Matatu Stages | tuples, unpacking | Stores stages as tuples and looks up a fare |
| [task8.py](task8.py) | Marks Table | list of lists | Averages rows and columns of a 2D list |

## Sample output

**Task 2: Weekly Sales Report**
```
Sales on Mon (KES): 4200
Sales on Tue (KES): 3850.5
Sales on Wed (KES): 5100
Sales on Thu (KES): 2975
Sales on Fri (KES): 6320
Sales on Sat (KES): 7480

Total sales:   KES 29,925.50
Average a day: KES 4,987.58
Best day:      Sat (KES 7,480.00)
Worst day:     Thu (KES 2,975.00)
```

**Task 6: Bubble Sort**
```
Prices before: [450, 120, 890, 60, 300]
After pass 1: [120, 450, 60, 300, 890]
After pass 2: [120, 60, 300, 450, 890]
After pass 3: [60, 120, 300, 450, 890]
After pass 4: [60, 120, 300, 450, 890]
Prices after:  [60, 120, 300, 450, 890]
Swaps made:    6
```

## Run a task

```bash
python task1.py
```

On Windows you can also use `py task1.py`; on Linux and macOS use `python3 task1.py`.
