"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Create the calculator's buttons.
"""
# IMPORTS: GUI library
import tkinter as tk
from tkinter.font import Font


class CalculatorButton(tk.Button):
    def __init__(self, master: tk.Frame, text: str, command):
        """ Class to create a button for the calculator"""
        super(CalculatorButton, self).__init__(
            master,
            text=text,
            command=command,
            relief=tk.RIDGE,
            font=Font(weight='bold'),
            bg='snow',
            activeforeground='OliveDrab1'
        )

    def place_button(self):
        """ Places a button in the frame."""
        self.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
