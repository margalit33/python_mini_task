# tools/numbers/comp.py

class CompModule:
    """
    A class to encapsulate various computational functions, enforcing that 
    functions from the simp module must be called first.

    Attributes:
        simp_called (bool): A flag indicating if functions from the simp module
                            have been called.
    """

    def __init__(self):
        """
        Initializes the CompModule instance, setting the simp_called flag to False.
        """
        self.simp_called = False

    def sum_of_digits(self, number):
        """
        Calculates the sum of the digits of a given number.

        Args:
            number (int): The number whose digits are to be summed.

        Returns:
            int: The sum of the digits of the given number.

        Raises:
            Exception: If functions from the simp module have not been called.
        """
        if not self.simp_called:
            raise Exception("Cannot call functions in comp module before calling simp module functions.")
        return sum(int(digit) for digit in str(number))

    def is_palindrome(self, number):
        """
        Checks if a given number is a palindrome.

        Args:
            number (int): The number to check.

        Returns:
            bool: True if the number is a palindrome, False otherwise.

        Raises:
            Exception: If functions from the simp module have not been called.
        """
        if not self.simp_called:
            raise Exception("Cannot call functions in comp module before calling simp module functions.")
        num_str = str(number)
        return num_str == num_str[::-1]

    def set_simp_called(self):
        """
        Sets the simp_called flag to True, indicating that functions from the simp module have been called.
        """
        self.simp_called = True

# Singleton instance of CompModule
comp_instance = CompModule()


