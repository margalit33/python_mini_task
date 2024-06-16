# tools/numbers/simp.py


from tools.numbers.comp import comp_instance

def add_numbers(a, b):
    """
    Adds two numbers together.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtracts the second number from the first number.

    Args:
        a (int, float): The number to be subtracted from.
        b (int, float): The number to subtract.

    Returns:
        int, float: The result of the subtraction.
    """
    return a - b

def some_function():
    """
    Calls a function from the comp module to set the simp_called flag to True.
    This ensures that functions in the comp module can be called without raising an exception.

    Side Effects:
        Sets comp_instance.simp_called to True.
    """
    comp_instance.set_simp_called()
    print("simp module function called, simp_called set to True")



