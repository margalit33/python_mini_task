# TASK2 Project

## Overview

This project demonstrates the use of custom Python modules organized in a directory structure. The project includes three main components:
- `simp` module: Provides basic arithmetic operations.
- `comp` module: Provides functions that depend on the `simp` module being called first.
- `col` module: Contains utility functions like zipping lists.

The `test_script.py` script tests the functionality of these modules.


## Modules

### `simp.py`
Contains basic arithmetic functions.
- `add_numbers(a, b)`: Returns the sum of `a` and `b`.
- `subtract_numbers(a, b)`: Returns the difference of `a` and `b`.
- `some_function()`: Sets a flag in the `comp` module.

### `comp.py`
Contains functions that operate on numbers.
- `sum_of_digits(number)`: Returns the sum of the digits of `number`.
- `is_palindrome(number)`: Checks if `number` is a palindrome.
- `set_simp_called()`: Sets an internal flag to allow the other functions to operate.

### `col.py`
Contains utility functions.
- `myzip(list1, list2)`: Zips two lists together.

## Usage

1. **Setup**
   Make sure you have Python 3 installed. It's recommended to use a virtual environment.
   
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   pip install pylint


