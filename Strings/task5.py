# Author: Daniel Otieno Odero - ICT Department, Delhi College
# Course: Python Programming - Strings Assignment
# Task 5: M-Pesa Message Reader
# Run with: python task5.py

message = ("QJK7TX2L9P Confirmed. Ksh1,250.00 sent to AMINA YUSUF 0712345678 "
           "on 30/9/26 at 10:15 AM. New M-PESA balance is Ksh3,480.50.")

# The code is everything before the first space
code = message[:message.find(" ")]

# The amount sits between "Ksh" and " sent"
start = message.find("Ksh") + 3
end = message.find(" sent")
amount = float(message[start:end].replace(",", ""))

# The name sits between "sent to " and the phone number
name_start = message.find("sent to ") + len("sent to ")
name_end = message.find(" 07")
name = message[name_start:name_end].title()

# The balance is the last Ksh value; strip the full stop at the end
balance_text = message[message.rfind("Ksh") + 3:].rstrip(".")
balance = float(balance_text.replace(",", ""))

print("Transaction code:", code)
print(f"Amount sent:      KES {amount:,.2f}")
print("Sent to:         ", name)
print(f"Balance left:     KES {balance:,.2f}")
