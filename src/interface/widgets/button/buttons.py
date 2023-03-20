"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create specific calculator's buttons.
"""

# IMPORT: GUI
import tkinter as tk

# IMPORT: Button
from .button import Button


class ClearButton(Button):
    def __init__(self, app: tk.Frame, master: tk.Frame):
        """
        Class to create a clear button for the calculator.

        Args:
            app (tk.Frame): master's master frame
            master (tk.Frame): button's master frame
        """
        super(ClearButton, self).__init__(app=app, master=master, text="CLEAR")

    def _command(self):
        """ Command to trigger when clicking the clear button. """
        return lambda: self._app.clear_str()


class ResultButton(Button):
    def __init__(self, app: tk.Frame, master: tk.Frame):
        """
        Class to create a result button for the calculator.

        Args:
            app (tk.Frame): master's master frame
            master (tk.Frame): button's master component
        """
        super(ResultButton, self).__init__(app=app, master=master, text="=")

    def _command(self):
        """ Command to trigger when clicking the result button. """
        return lambda: self._app.display_result()


class DecimalButton(Button):
    def __init__(self, app: tk.Frame, master: tk.Frame):
        """
        Class to create a decimal button for the calculator.

        Args:
            app (tk.Frame): master's master frame
            master (tk.Frame): button's master component
        """
        super(DecimalButton, self).__init__(app=app, master=master, text=".")

    def _command(self):
        """ Command to trigger when clicking the decimal button. """
        return lambda: self._app.add_str(self._text)


class DigitButton(Button):
    def __init__(self, app: tk.Frame, master: tk.Frame, value: int):
        """
        Class to create digits buttons for the calculator.

        Args:
            app (tk.Frame): master's master frame
            master (tk.Frame): button's master component
            value (int): digit
        """
        super(DigitButton, self).__init__(app=app, master=master, text=str(value))

    def _command(self):
        """ Command to trigger when clicking a digit button. """
        return lambda: self._app.add_str(self._text)


class OperatorButton(Button):
    def __init__(self, app: tk.Frame, master: tk.Frame, value: str):
        """
        Class to create operator buttons for the calculator.

        Args:
            app (tk.Frame): master's master frame
            master (tk.Frame): button's master component
            value (str): operator
        """
        super(OperatorButton, self).__init__(app=app, master=master, text=value)

    def _command(self):
        """ Command to trigger when clicking an operator button. """
        return lambda: self._app.add_str(self._text)
