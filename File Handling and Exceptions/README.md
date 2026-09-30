# Python File Handling and Exceptions

Eight intermediate tasks on reading and writing text and CSV files, and handling errors with `try`, `except`, `else` and `finally`.

## Tasks

| File | Task | Covers | What it does |
|---|---|---|---|
| [task1.py](task1.py) | Notice Board Reader | reading lines | Numbers each line of a text file and counts words |
| [task2.py](task2.py) | Save a Class List | writing `"w"` | Writes a class list to a new file and reads it back |
| [task3.py](task3.py) | Visitors Log | appending `"a"` | Appends a visit to a log file |
| [task4.py](task4.py) | Safe Number Input | `try`/`except` | Validates whole-number input with `try`/`except` |
| [task5.py](task5.py) | Marks From a CSV File | `csv.DictReader` | Reads a CSV of marks and grades each student |
| [task6.py](task6.py) | Fee Balance Report | CSV in, report out | Writes a report of students with fee balances |
| [task7.py](task7.py) | Open Any File | `else`, `finally` | Opens a named file, handling a missing one |
| [task8.py](task8.py) | M-Pesa Statement | `csv.reader`, bad data | Totals a statement and reports bad rows |

## Sample data

The tasks read these sample files. Run each task from inside this folder so Python can find them. Tasks 2 and 6 create new files (`class_list.txt` and `fee_report.txt`) when they run.

- [fees.csv](fees.csv)
- [marks.csv](marks.csv)
- [mpesa_statement.csv](mpesa_statement.csv)
- [notices.txt](notices.txt)
- [visitors_log.txt](visitors_log.txt)

## Sample output

**Task 6: Fee Balance Report**
```
Report saved to fee_report.txt (3 students owing).
```

Contents of `fee_report.txt` afterwards:
```
FEE BALANCE REPORT - DELHI COLLEGE
DC104  Kevin Mutua      KES   7,500
DC112  Omar Farah       KES  24,000
DC118  Wanjiku Mwangi   KES   6,000
Students owing: 3
Total owed: KES 37,500
```

**Task 8: M-Pesa Statement**
```
Line 7: bad amount 'one thousand'
Line 9: bad amount ''

Money in:   KES  68,000.00
Money out:  KES  24,550.50
Net change: KES  43,449.50
Rows skipped: 2
```

## Run a task

```bash
python task1.py
```

On Windows you can also use `py task1.py`; on Linux and macOS use `python3 task1.py`.

Run the tasks from inside this folder so they can find the sample data files.
