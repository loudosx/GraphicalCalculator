"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Preprocess the calculation string & dictionary to feed the Calculator Computer.
"""


class PreProcessor:
    def __init__(self):
        # Attributes
        self._OPERATORS = ['*', '/', '-', '+']
        self._DIGITS = [str(digit) for digit in range(10)]

    def _calculation_as_list(self, calculation: str) -> list:
        """
        Splits the calculation string (by operators & operands).

        Args:
            calculation (str): string to split

        Returns:
            list: split calculation string as a list
        """
        if not calculation:
            raise ValueError("The string is empty.")

        calculation_as_list = ['']
        for elem in calculation:
            if elem in self._OPERATORS:
                calculation_as_list.append(elem)
                calculation_as_list.append('')
            else:
                calculation_as_list[-1] += elem

        if '' in calculation_as_list:
            raise ValueError("Two operators are following each other.")

        for idx, elem in enumerate(calculation_as_list):
            if elem not in self._OPERATORS:
                calculation_as_list[idx] = float(elem)

        return calculation_as_list


    def _calculation_as_dict(self, calculation: list) -> dict:
        """
        Retrieves elements of the calculation string for computation.

        Args:
            calculation (list): calculation's string as a list

        Returns:
            calculation_as_dict (dict): calculation's string as
        """
        calculation_as_dict = {
            'operators': dict(),
            'operands': dict()
        }

        for idx, elem in enumerate(calculation):
            # OPERATORS
            if elem in self._OPERATORS:
                if elem not in calculation_as_dict['operators']:
                    calculation_as_dict['operators'][elem] = list()
                calculation_as_dict['operators'][elem].append(idx)

            # OPERANDS
            else:
                if elem not in calculation_as_dict['operands']:
                    calculation_as_dict['operands'][elem] = list()
                calculation_as_dict['operands'][elem].append(idx)

        return calculation_as_dict

    def _order_operators(self, calculation: dict) -> list:
        """
        Orders operators based on maths' prioritization.

        Returns:
             list: ordered operators' positions
        """
        ordered_calculation = list()
        for operator in self._OPERATORS:
            if operator in calculation['operators']:
                ordered_calculation.extend(calculation['operators'][operator])

        return ordered_calculation

    def __call__(self, calculation: str):
        """
        Preprocesses the calculation's string.

        Args:
            calculation (str): calculation's string

        Returns:
            list: ordered operators' positions list
            calculation_as_list (list): calculation's string as a list
        """
        calculation_as_list = self._calculation_as_list(calculation)
        calculation_as_dict = self._calculation_as_dict(calculation_as_list)

        return self._order_operators(calculation_as_dict), calculation_as_list
