"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Create the calculator's frames.
"""
# IMPORTS: GUI library
import tkinter as tk


class CalculatorFrame(tk.Frame):
    def __init__(self, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        super(CalculatorFrame, self).__init__(
            master,
            padx=padx,
            pady=pady,
            borderwidth=borderwidth,
            bg='snow'
        )
        self.pack(fill=tk.BOTH, expand=True)
