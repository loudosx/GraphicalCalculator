"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Create the calculator's display box.
"""
# IMPORTS: GUI library
import tkinter as tk
from tkinter.font import Font


class CalculatorBox(tk.Text):
    def __init__(self, master: tk.Frame, height: int, width: int):
        """ Class to create a box able to display text. """
        super(CalculatorBox, self).__init__(
            master,
            height=height,
            width=width,
            wrap='word',
            font=Font(family='Courier', size=20, slant='italic')
        )
        self.insert('1.0', 'Use the buttons below to enter what needs to be computed')

    def display_text(self, text: str):
        """
        Displays text in the corresponding box.

        Args:
            text (str): text to display
        """
        self.config(font=('Courier', 25))
        self.clear_box()
        self.insert('1.0', text)

    def clear_box(self):
        self.delete('1.0', 'end-1c')

    def _get_text(self):
        return self.get('1.0', 'end-1c')
