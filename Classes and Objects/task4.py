# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 4: Marks With Validation
# Run with: python task4.py

class Result:
    """A unit result whose mark must stay between 0 and 100."""

    def __init__(self, unit, mark):
        self.unit = unit
        self.set_mark(mark)

    def set_mark(self, mark):
        if 0 <= mark <= 100:
            self._mark = mark
        else:
            print(f"  {mark} is not a valid mark for {self.unit}. Using 0.")
            self._mark = 0

    def get_mark(self):
        return self._mark

    def grade(self):
        if self._mark >= 70:
            return "A"
        elif self._mark >= 60:
            return "B"
        elif self._mark >= 50:
            return "C"
        elif self._mark >= 40:
            return "D"
        return "E"


results = []
for unit in ["Python", "Web Design", "Networking"]:
    mark = int(input(f"Mark for {unit}: "))
    results.append(Result(unit, mark))

print()
for r in results:
    print(f"{r.unit:<12}{r.get_mark():>4}  {r.grade()}")
