"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Prepare the calculation string & dictionary to feed the Calculator Computer.
"""
# IMPORTS: Utils
import numpy as np
from src.utils.utils import invert_dic


class Preparator:
    def __init__(self, calculation_str: str):
        self._dic_elements = dict()
        self._calculation_str = calculation_str

        self._operators_list = ['+', '-', '*', '/']
        self._numbers_list = [str(n) for n in np.arange(0, 10)]

    def split_calculation_str(self, calculation_str: str) -> list[str]:
        """
        Splits the calculation string (by numbers & symbols).

        Args:
            calculation_str (str): string to split

        Returns:
            list[str]: list of split calculation string
        """
        if len(calculation_str) == 0:
            return list(calculation_str)

        else:
            calculation_str_split = calculation_str[0]

            for i in range(0, len(calculation_str) - 1):
                # If next string's char is an operator, add it with blank spaces before & after.
                if calculation_str[i + 1] in self._operators_list:
                    calculation_str_split += ' ' + calculation_str[i + 1] + ' '
                # If next string's char is a number or a dot, add it as is.
                if (calculation_str[i + 1] in self._numbers_list) or \
                        (calculation_str[i + 1] == '.'):
                    calculation_str_split += calculation_str[i + 1]

            return calculation_str_split.split()

    def get_elements(self):
        """
        Retrieves elements of the calculation string for computation.

        Returns:
            nb_operations (int): number of operations to compute
        """
        self._dic_elements = {
            'operators': {},
            'operands': {}
        }

        for i, e in enumerate(self._calculation_str):
            if e in self._operators_list:
                self._dic_elements['operators'][i] = e

            elif float(e):
                self._dic_elements['operands'][i] = str(float(e))

        nb_operations = len(self._dic_elements['operators'])
        self._dic_elements['operators'] = invert_dic(self._dic_elements['operators'])
        self._dic_elements['operands'] = invert_dic(self._dic_elements['operands'])

        return self._dic_elements, nb_operations
