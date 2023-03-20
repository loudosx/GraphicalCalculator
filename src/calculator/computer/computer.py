"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Compute the content of the calculation string recovered from the Calculator App's display
box.
"""
from src.calculator.computer.updater.updater import Updater


class Computer:
    def __init__(self, dic_elements: dict, nb_op: int, calculation_str=None):
        self._dic_elements = dic_elements
        self._calculation_str = calculation_str
        self._nb_op = nb_op
        self._updater = Updater(self._calculation_str, self._dic_elements)

    def _order_operators(self) -> list:
        """
        Orders operators based on the prioritization in maths.

        Returns:
             list: list of the ordered operators' positions
        """
        ordered_operator_positions = list()
        symbols = [s for s in self._dic_elements['operators']]

        if '*' in symbols:
            ordered_operator_positions.extend([s for s in self._dic_elements['operators']['*']])

        if '/' in symbols:
            ordered_operator_positions.extend([s for s in self._dic_elements['operators']['/']])

        if '-' in symbols:
            ordered_operator_positions.extend([s for s in self._dic_elements['operators']['-']])

        if '+' in symbols:
            ordered_operator_positions.extend([s for s in self._dic_elements['operators']['+']])

        return ordered_operator_positions

    @staticmethod
    def _compute_sum(a: float, b: float) -> float:
        """
        Computes the sum of two operands.

        Args:
            a (float): first operand
            b (float): second operand

        Returns:
            float: sum of the two operands
        """
        return a + b

    @staticmethod
    def _compute_difference(a: float, b: float) -> float:
        """
        Computes the difference of two operands.

        Args:
            a (float): left operand
            b (float): right operand

        Returns:
            float: difference of the two operands
        """
        return a - b

    @staticmethod
    def _compute_division(a: float, b: float) -> float:
        """
        Computes the division of two operands.

        Args:
            a (float): first operand
            b (float): second operand

        Returns:
            float: division of the two operands
        """
        return a / b

    @staticmethod
    def _compute_multiplication(a: float, b: float) -> float:
        """
        Computes the multiplication of two operands.

        Args:
            a (float): first operand
            b (float): second operand

        Returns:
            float: multiplication of the two operands
        """
        return a * b

    def compute_calculation(self) -> str:
        """
        Computes the different calculations.

        Returns:
            calculation (str): the result of calculation as a string
        """
        calculation = 0

        for i in range(self._nb_op):
            ordered_operator_positions = self._order_operators()
            ordered_pos = ordered_operator_positions[0]
            operator = self._calculation_str[ordered_pos]

            l_operand = float(self._calculation_str[ordered_pos-1])
            r_operand = float(self._calculation_str[ordered_pos+1])

            if operator == '*':
                calculation = str(Computer._compute_multiplication(l_operand, r_operand))

            if operator == '/':
                calculation = str(Computer._compute_division(l_operand, r_operand))

            if operator == '+':
                calculation = str(Computer._compute_sum(l_operand, r_operand))

            if operator == '-':
                calculation = str(Computer._compute_difference(l_operand, r_operand))

            self._calculation_str = self._updater.update_calculation_string(
                ordered_pos,
                calculation
            )
            self._dic_elements = self._updater.update_key_values(
                ordered_pos,
                l_operand,
                r_operand,
                operator,
                calculation
            )

            self._dic_elements = self._updater.update_value_values(ordered_pos)

        return calculation
