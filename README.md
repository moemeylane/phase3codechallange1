# phase3codechallange1
Python Coding Assessment
This repository contains solutions for a Python coding assessment designed to evaluate fundamental Python concepts, including basic data structures, functions, decorators, sequences, sets, dictionaries, and object-oriented programming.


# Setup Instructions
Clone the Repository

` git clone git@github.com:moemeylane/phase3codechallange1.git`
cd -repo-name `phase3codechallange1`

# To run the code
python your_script_name.py

# Summary of Functions and Class
1. add_numbers
Purpose: Adds two numbers and returns their sum.

`def add_numbers(num1, num2):
    return num1 + num2`

2. is_even
Purpose: Checks if a number is even. Returns True if it is, and False otherwise.

`def is_even(number):
    return number % 2 == 0`
3. reverse_string
Purpose: Reverses a given string and returns the reversed version.

`def reverse_string(text):
    return text[::-1]`

4. count_vowels
Purpose: Counts the number of vowels (a, e, i, o, u) in a given string, ignoring case.

`def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)`
5. calculate_factorial
Purpose: Calculates the factorial of a non-negative integer. The factorial of a number n is the product of all positive integers less than or equal to n.

`def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial`
6. apply_decorator
Purpose: Applies a decorator function that prints "Decorator Applied" before executing the given function.

`def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func`
7. sort_by_age
Purpose: Sorts a list of tuples (where each tuple contains a name and an age) by the age in ascending order using operator.itemgetter.

`import operator

def sort_by_age(tuples_list):
    return sorted(tuples_list, key=operator.itemgetter(1))`

8. merge_dicts
Purpose: Merges two dictionaries into one. If there are common keys, their values are summed up.

`def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict`
9. Car Class
Purpose: Defines a class to represent a car with attributes for make, model, and year. Includes a method to display the car's information.

`class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")`


