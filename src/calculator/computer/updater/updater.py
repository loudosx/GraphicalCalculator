"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Update the calculation's string & dictionary as computation is being done.
"""
# IMPORTS: utils
import numpy as np


class Updater:
    def __init__(self, calculation_str: list[str], dic_elements: dict):
        """ Class to update the dictionary and calculation string during computation. """
        self._calculation_str = calculation_str
        self._dic_elements = dic_elements

    def _add_calculation_result(self, res: str, pos: int) -> dict:
        """ Adds the calculation result to the dictionary.

        Args:
            res (str): result to add to the dictionary
            pos (float): position to add the result to

        Returns:
            self._dic_elements (dict): updated dictionary with calculation result
        """

        if res in self._dic_elements['operands']:
            self._dic_elements['operands'][res].append(pos-1)
        else:
            self._dic_elements['operands'][res] = [pos-1]

        return self._dic_elements

    def _remove_operands_operator(
            self,
            a: float,
            b: float,
            operator: str,
            pos: int
    ) -> dict:
        """
        Removes operands and operator used during the computation from the dictionary.

        Args:
            a (float): left operand to remove
            b (float): right operand to remove
            operator (str): operator to remove
            pos (str): position of the operator

        Returns:
            self._dic_elements (dict): updated dictionary
        """
        a, b = str(a), str(b)
        # Removes left operand from dictionary
        # If the operand is found at least twice in the dictionary
        if len(self._dic_elements['operands'][a]) > 1:
            self._dic_elements['operands'][a].remove(pos-1)
        # If the operand is found once
        else:
            self._dic_elements['operands'].pop(a)

        # Removes right operand from dictionary
        if len(self._dic_elements['operands'][b]) > 1:
            self._dic_elements['operands'][b].remove(pos+1)
        else:
            self._dic_elements['operands'].pop(b)

        # Removes operator from dictionary
        self._dic_elements['operators'][operator].pop(0)

        return self._dic_elements

    def update_key_values(
            self,
            pos: int,
            a: float,
            b: float,
            operator: str,
            res: str
    ) -> dict:
        """
        Updates dictionary keys when they have been used for computation.

        Args:
            pos (int): operator's index
            a (float): left operand used
            b (float): right operand used
            operator (str): operator used
            res (str): result of the computation as a string

        Returns:
            dic_elements (dic): the updated dictionary
        """
        self._dic_elements = self._add_calculation_result(res, pos)
        self._dic_elements = self._remove_operands_operator(a, b, operator, pos)

        return self._dic_elements

    def update_value_values(self, pos: int) -> dict:
        """
        Updates dictionary's keys values (positions in the string) as the calculation is computed.

        Args:
            pos (int): position of the operator used for the calculation

        Returns:
            updated_dic_elements (dict): updated dictionary
        """
        # Dictionary to update positions' values
        diff_dic_elements = {
            'operators':
                {x: list(np.full(len(self._dic_elements['operators'][x]), 2))
                 for x in self._dic_elements['operators']
                 },
            'operands':
                {x: list(np.full(len(self._dic_elements['operands'][x]), 2))
                 for x in self._dic_elements['operands']
                 }
        }

        updated_dic_elements = self._dic_elements.copy()
        updated_dic_elements['operators'] = {
            operator: list(
                map(
                    int,
                    list(
                        map(
                            lambda x: x - diff_dic_elements['operators'][operator][i],
                        updated_dic_elements['operators'][operator]
                        )
                    )
                )) if self._dic_elements['operators'][operator][i] > pos
            else list(
                map(
                    int,
                    list(
                        map(
                            lambda x: updated_dic_elements['operators'][operator][i],
                                updated_dic_elements['operators'][operator]
                        )
                    ),
                )
            )
            for operator in updated_dic_elements['operators']
            for i in range(len(updated_dic_elements['operators'][operator]))
        }

        updated_dic_elements['operands'] = {
            operand: list(
                map(
                    int,
                    list(
                        map(
                            lambda x: x - diff_dic_elements['operands'][operand][i],
                                updated_dic_elements['operands'][operand]
                        )
                    )
                )
            )
            if self._dic_elements['operands'][operand][i] > pos
            else list(
                map(
                    int,
                    list(
                        map(
                            lambda x: updated_dic_elements['operands'][operand][i],
                                updated_dic_elements['operands'][operand]
                        )
                    ),
                )
            ) for operand in updated_dic_elements['operands']
            for i in range(len(updated_dic_elements['operands'][operand]))
        }

        print(updated_dic_elements['operands'])
        self._dic_elements = updated_dic_elements
        return updated_dic_elements

    def update_calculation_string(self, pos: int, res: str):
        """
        Updates the calculation string as the calculation is computed.

        Args:
            pos (int): original position of the operator associated with the calculation
            res (str): result of the calculation as a string
        """
        self._calculation_str[pos-1] = res
        self._calculation_str.pop(pos)
        self._calculation_str.pop(pos)

        return self._calculation_str
