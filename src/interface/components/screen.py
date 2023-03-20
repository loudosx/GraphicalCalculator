"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create the calculator's screen.
"""

# IMPORTS: GUI
import tkinter as tk
from tkinter.font import Font


class Screen(tk.Text):
    def __init__(self, master: tk.Frame, height: int, width: int):
        """
        Class to create a box able to display text.

        Args:
            master (tk.Frame): screen's master frame
            height (int): screen's height
            width (int): screen's width
        """
        default_params = {"font": Font(family='Courier', size=16, slant='italic')}

        super(Screen, self).__init__(
            master,
            height=height, width=width, wrap='word',
            **default_params
        )

        self.insert('1.0', 'Use the buttons below to enter what needs to be computed')
        self.display()

    def display_text(self, text: str):
        """
        Displays text in the corresponding screen.

        Args:
            text (str): text to display
        """
        self.config(font=('Courier', 25))
        self.clear_box()
        self.insert('1.0', text)

    def clear_box(self):
        """ Clears the screen. """
        self.delete('1.0', 'end-1c')

    def _get_text(self):
        """ Retrieves the screen's text. """
        return self.get('1.0', 'end-1c')

    def display(self):
        """ Places the screen. """
        self.configure(bg='light cyan', foreground='light sea green')
        self.pack(fill=tk.BOTH, expand=True)
