#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
if number < 0:
    last_digit = -(-number % 10)  # Ensures the last digit of negative numbers is negative
else:
    last_digit = number % 10

# Print the base message
print(f"Last digit of {number} is {last_digit}", end=" ")

# Check conditions for last digit and print the appropriate message
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")