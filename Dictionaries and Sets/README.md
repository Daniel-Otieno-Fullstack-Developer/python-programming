# Python Dictionaries and Sets

Eight beginner tasks on dictionaries (records, lookups, counting and nested records) and sets (removing duplicates and comparing groups).

## Tasks

| File | Task | Covers | What it does |
|---|---|---|---|
| [task1.py](task1.py) | Student Record | keys, `items()` | Reads, changes and lists a dictionary record |
| [task2.py](task2.py) | Price List | `get()` | Looks up a price with `get()` |
| [task3.py](task3.py) | Phone Book | add, `del`, `in` | A menu-driven phone book |
| [task4.py](task4.py) | Word Frequency | counting with `get()` | Counts words and draws a bar for each |
| [task5.py](task5.py) | Stock Tracker | updating values | Updates stock levels and flags reorders |
| [task6.py](task6.py) | Class Results | nested dictionaries | Reports averages and grades from nested records |
| [task7.py](task7.py) | Club Members | `&`, `|`, `-`, `^` | Compares two groups with `&`, `|`, `-`, `^` |
| [task8.py](task8.py) | Unique Visitors | `set()`, counting | Removes duplicates with a set and counts visits |

## Sample output

**Task 5: Stock Tracker**
```
How many sales to record? 3
Item sold: sugar
Quantity: 15
Item sold: cooking oil
Quantity: 5
Item sold: rice
  Unknown item.

STOCK LEVELS
sugar         25
maize flour   25
cooking oil    7  <- reorder
salt          30
```

**Task 7: Club Members**
```
Coding club: ['Amina', 'Brian', 'Chebet', 'Dahir', 'Esther']
Football:    ['Brian', 'Dahir', 'Farah', 'Grace']
In both:           ['Brian', 'Dahir']
In either:         ['Amina', 'Brian', 'Chebet', 'Dahir', 'Esther', 'Farah', 'Grace']
Coding only:       ['Amina', 'Chebet', 'Esther']
Only one of them:  ['Amina', 'Chebet', 'Esther', 'Farah', 'Grace']
Who wants to join coding club? Farah
Farah added. Members now: 6
```

## Run a task

```bash
python task1.py
```

On Windows you can also use `py task1.py`; on Linux and macOS use `python3 task1.py`.
