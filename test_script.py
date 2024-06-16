"""
This script tests the functionality of the tools.numbers.simp and tools.numbers.comp modules,
as well as the tools.col module.
"""

import sys
import os
from tools.numbers.simp import some_function, add_numbers, subtract_numbers
from tools.numbers.comp import comp_instance
from tools import col

# Append the tools directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'tools')))

# Call the simp module function to set simp_called to True
some_function()

# Test simp module functions
result_of_addition = add_numbers(10, 4)  # pylint: disable=invalid-name
result_of_subtraction = subtract_numbers(10, 12)  # pylint: disable=invalid-name

print("Result of adding:", result_of_addition)
print("Result of subtracting:", result_of_subtraction)

# Test comp module functions
try:
    result_sum_of_digits = comp_instance.sum_of_digits(123)  # pylint: disable=invalid-name
except RuntimeError as e:
    print("Exception caught:", e)

comp_instance.set_simp_called()  # Simulate calling simp functions

result_sum_of_digits = comp_instance.sum_of_digits(123)  # pylint: disable=invalid-name
result_is_palindrome = comp_instance.is_palindrome(1234)  # pylint: disable=invalid-name

print("Sum of digits:", result_sum_of_digits)
print("Is palindrome:", result_is_palindrome)

# Test col module function
list1 = [10, 20, 30]
list2 = ['a', 'b', 'c']

zipped = col.myzip(list1, list2)
print("Zipped result:", list(zipped))



