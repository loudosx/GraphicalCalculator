"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Create the calculator backend.
"""
# IMPORT: Calculation String Computer
from src.calculator.computer.computer import Computer

# IMPORT: Calculation String Preparator
from src.calculator.preparator.preparator import Preparator


class Calculator:
    def __init__(self, calculation_str: str):
        """ Class corresponding to the backend of the graphical calculator. """
        self._preparator = Preparator(calculation_str)
        self._dic_elements, self._nb_op = self._preparator.get_elements()
        self._calculation_str = self._preparator.split_calculation_str(calculation_str)
        self._computer = Computer(self._dic_elements, self._nb_op, self._calculation_str)

    def __call__(self):
        """
        Computes the different calculations.

        Returns:
            calculation (str): the result of calculation as a string
        """
        return self._computer.compute_calculation()
