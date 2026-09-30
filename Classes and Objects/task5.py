# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Classes and Objects Assignment
# Task 5: Gate Counter
# Run with: python task5.py

class GateCounter:
    """Counts people in and out of the college gate."""

    total_gates = 0                     # class attribute: shared by all gates

    def __init__(self, name):
        self.name = name
        self.inside = 0
        GateCounter.total_gates += 1

    def enter(self, people=1):
        self.inside += people

    def leave(self, people=1):
        # never let the count go below zero
        self.inside = max(0, self.inside - people)

    def __str__(self):
        return f"{self.name}: {self.inside} inside"


main_gate = GateCounter("Main gate")
back_gate = GateCounter("Back gate")

main_gate.enter(25)
main_gate.leave(7)
back_gate.enter(4)
back_gate.leave(10)

print(main_gate)                        # print() uses __str__
print(back_gate)
print("Gates being counted:", GateCounter.total_gates)
