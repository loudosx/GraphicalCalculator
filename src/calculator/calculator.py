"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create the calculator backend.
"""

# IMPORTS: Preprocessor & Computer
from src.calculator.pre_processor import PreProcessor
from src.calculator.computer import Computer


class Calculator:
    def __init__(self):
        """ Class corresponding to the backend of the graphical calculator. """
        self._pre_processor = PreProcessor()
        self._computer = Computer()

    def __call__(self, calculation: str) -> str:
        """
        Computes the calculation string's content.

        Args:
            calculation (str): calculation's string

        Returns:
            calculation (str): the result of calculation as a string
        """
        ordered_operators, calculation = self._pre_processor(calculation)
        return self._computer(ordered_operators, calculation)
