#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else ((-number % 10) * -1)
string = f"Last digit of {number}"
if last_digit > 5:
    print(string, "is {} and is greater than 5".format(last_digit))
elif last_digit == 0:
    print(string, "is {} and is 0".format(last_digit))
elif last_digit < 6 and not 0:
    print(string, "is {} and is less than 6 and not 0".format(last_digit))
