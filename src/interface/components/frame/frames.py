"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19
@Purpose: Create specific calculator's frames.
"""

# IMPORT: GUI
import tkinter as tk

# IMPORTS: Calculator's Frame & Widgets
from .frame import Frame
from src.interface.widgets import ClearButton, ResultButton, DecimalButton, DigitButton, \
    OperatorButton


class OperatorsFrame(Frame):
    def __init__(self, app, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        """
        Class to create the frame containing operators' buttons.

        Args:
            master (tk.Tk): master's frame
            padx (int): padding on the frame's x axis
            pady (int): padding on the frame's y axis
            borderwidth (int): width of the frame's border
        """
        super(OperatorsFrame, self).__init__(master, padx=padx, pady=pady, borderwidth=borderwidth)

        self._buttons = {
            "0": OperatorButton(app, self, value='/'),
            "1": OperatorButton(app, self, value='*'),
            "2": OperatorButton(app, self, value='-'),
            "3": OperatorButton(app, self, value='+')
        }


class Digits1Frame(Frame):
    def __init__(self, app, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        """
        Class to create the first frame containing digits' buttons.

        Args:
            master (tk.Tk): master's frame
            padx (int): padding on the frame's x axis
            pady (int): padding on the frame's y axis
            borderwidth (int): width of the frame's border
        """
        super(Digits1Frame, self).__init__(master, padx=padx, pady=pady, borderwidth=borderwidth)

        self._buttons = {
            "0": DigitButton(app, self, value=7),
            "1": DigitButton(app, self, value=8),
            "2": DigitButton(app, self, value=9),
        }


class Digits2Frame(Frame):
    def __init__(self, app, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        """
        Class to create the second frame containing digits' buttons.

        Args:
            master (tk.Tk): master's frame
            padx (int): padding on the frame's x axis
            pady (int): padding on the frame's y axis
            borderwidth (int): width of the frame's border
        """
        super(Digits2Frame, self).__init__(master, padx=padx, pady=pady, borderwidth=borderwidth)

        # Components
        self._buttons = {
            "0": DigitButton(app, self, value=4),
            "1": DigitButton(app, self, value=5),
            "2": DigitButton(app, self, value=6),
        }


class Digits3Frame(Frame):
    def __init__(self, app, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        """
        Class to create the third frame containing digits' buttons.

        Args:
            master (tk.Tk): master's frame
            padx (int): padding on the frame's x axis
            pady (int): padding on the frame's y axis
            borderwidth (int): width of the frame's border
        """
        super(Digits3Frame, self).__init__(master, padx=padx, pady=pady, borderwidth=borderwidth)

        self._buttons = {
            "0": DigitButton(app, self, value=1),
            "1": DigitButton(app, self, value=2),
            "2": DigitButton(app, self, value=3),
        }


class OptionsFrame(Frame):
    def __init__(self, app, master: tk.Tk, padx=None, pady=None, borderwidth=None):
        """
        Class to create the frame containing options' buttons.

        Args:
            master (tk.Tk): master's frame
            padx (int): padding on the frame's x axis
            pady (int): padding on the frame's y axis
            borderwidth (int): width of the frame's border
        """
        super(OptionsFrame, self).__init__(master, padx=padx, pady=pady, borderwidth=borderwidth)

        self._buttons = {
            "0": ClearButton(app, self),
            "1": DigitButton(app, self, value=0),
            "2": DecimalButton(app, self),
            "3": ResultButton(app, self)
        }
