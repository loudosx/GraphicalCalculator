"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create a general frame for the calculator.
"""

# IMPORT: GUI
import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        """
        Class to create a frame.

        Args:
            master (tk.Tk): frame's master component
            padx (int): padding on the frame's x axis
            pady (int): padding on the frame's y axis
            borderwidth (int): width of the frame's border
        """
        default_params = {"bg": "snow"}

        super(Frame, self).__init__(
            master,
            padx=padx, pady=pady, borderwidth=borderwidth,
            **default_params
        )

        self.display()

    def display(self):
        """ Places a frame in its master component."""
        self.pack(fill=tk.BOTH, expand=True)
