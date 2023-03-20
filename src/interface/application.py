"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create the calculator's interface.
"""

# IMPORT: GUI
import tkinter as tk

# IMPORTS: Calculator's BackEnd & Components
from src.calculator.calculator import Calculator
from .components import Screen, Frame, OperatorsFrame, Digits1Frame, Digits2Frame, \
    Digits3Frame, OptionsFrame


class CalculatorApp(tk.Frame):
    def __init__(self):
        """Class to create the calculator's interface."""
        self._master = tk.Tk()
        self._master.geometry('300x500')
        self._master.title("Handmade Python Calculator")

        super(CalculatorApp, self).__init__(self._master)

        self._calculator = Calculator()
        self._calculation_str = ""

        # Components
        first_frame = Frame(self._master, pady=10, borderwidth=2)
        self._display_box = Screen(first_frame, 2, 20)

        OperatorsFrame(self, self._master, padx=3)
        Digits1Frame(self, self._master, padx=3)
        Digits2Frame(self, self._master, padx=3)
        Digits3Frame(self, self._master, padx=3)
        OptionsFrame(self, self._master, padx=3)

        # Launch
        self._master.mainloop()

    def clear_str(self):
        """ Clears the calculation string. """
        self._calculation_str = ''
        self._display_box.display_text(self._calculation_str)
        self._display_box.config(state='normal')

    def add_str(self, char: str):
        """
        Adds the character, corresponding to the button clicked, to the calculation string.

        Args:
            char (str): character to add
        """
        self._calculation_str += char
        self._display_box.display_text(self._calculation_str)

    def display_result(self):
        """ Displays the result of the calculation string. """
        self._calculation_str = self._calculator(self._calculation_str)
        self._display_box.display_text(self._calculation_str)
