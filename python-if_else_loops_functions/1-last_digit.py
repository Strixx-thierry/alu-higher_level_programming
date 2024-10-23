#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit
last_digit = abs(number) % 10  # This gets the absolute last digit
if number < 0:
    last_digit = -last_digit  # Make it negative if the number is negative

# Print the output
print(f"Last digit of {number} is {last_digit} ", end="")

# Determine the message based on the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
