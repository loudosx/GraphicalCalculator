"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create a general calculator's button.
"""

# IMPORTS: GUI
import tkinter as tk
from tkinter.font import Font


class Button(tk.Button):
    def __init__(self, app: tk.Frame, master: tk.Frame, text: str):
        """
        Class to create a button for the calculator.

        Args:
            app (tk.Frame): master's master frame
            master (tk.Frame): button's master frame
            text (str): text displayed on the button
        """
        default_params = {
            "relief": tk.RIDGE, "font": Font(weight="bold"),
            "bg": "snow", "activeforeground": "OliveDrab1"
        }

        super(Button, self).__init__(
            master,
            text=text, command=self._command(),
            **default_params
        )

        self._app = app
        self._text = text

        self.display()

    def display(self):
        """ Places a button in the frame. """
        self.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

    def _command(self):
        """ Abstract method. """
        raise NotImplementedError()
