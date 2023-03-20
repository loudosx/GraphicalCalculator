"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Compute the content of the calculation string recovered from the Calculator App's display
box.
"""


class Computer:
    def __init__(self):
        """ Class to create the calculations' computer."""
        # Attributes
        self._operations = {
            "*": lambda x,y: x*y,
            "/": lambda x,y: x/y,
            "-": lambda x,y: x-y,
            "+": lambda x,y: x+y,
        }

    def _compute_calculation(self, ordered_operators: list, calculation: list) -> str:
        """
        Computes the different calculations.

        Args:
            ordered_operators (list): positions of operators ordered by priority
            calculation (list): calculation's string as a list

        Returns:
            calculation (str): the result of calculation as a string
        """
        for i in range(len(ordered_operators)):
            operator_idx = ordered_operators[i]

            # Calculation
            left_op, operator, right_op = calculation[operator_idx-1:operator_idx+2]
            ope_result = self._operations[operator](left_op, right_op)

            # Update
            calculation = calculation[:operator_idx-1] + calculation[operator_idx+2:]
            calculation.insert(operator_idx-1, ope_result)

            for idx, position in enumerate(ordered_operators):
                if position > operator_idx:
                    ordered_operators[idx] -= 2

        return str(round(calculation[0], 3))

    def __call__(self, ordered_operators: list, calculation: list) -> str:
        """
        Computes calculations.

        Args:
            ordered_operators (list): positions of operators ordered by priority
            calculation (list):  calculation's string as a list

        Returns:
            str: calculation's result
        """
        return self._compute_calculation(ordered_operators, calculation)
