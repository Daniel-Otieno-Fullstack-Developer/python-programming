# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Functions Assignment
# Task 4: Fare With Discount
# Run with: python task4.py

def fare_to_pay(fare, discount=0, student=False):
    """Return the fare after a discount (in %) and a KES 20 student reduction."""
    amount = fare - fare * discount / 100
    if student:
        amount -= 20
    return amount


fare = float(input("Normal fare (KES): "))

print("Full fare:            KES", fare_to_pay(fare))
print("10% discount:         KES", fare_to_pay(fare, 10))
print("Student fare:         KES", fare_to_pay(fare, student=True))
print("Student + 10% off:    KES", fare_to_pay(fare, discount=10, student=True))
