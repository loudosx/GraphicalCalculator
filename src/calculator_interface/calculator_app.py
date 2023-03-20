"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
@Purpose: Create the calculator's interface.
"""
# IMPORT: GUI library
import tkinter as tk

# IMPORT: Calculator Computer
from src.calculator.calculator import Calculator

# IMPORT: Calculator Widgets
from src.calculator_interface.widgets.box import CalculatorBox
from src.calculator_interface.widgets.button import CalculatorButton
from src.calculator_interface.widgets.frame import CalculatorFrame


class CalculatorApp(tk.Frame):
    def __init__(self, master: tk.Tk):
        """Class to create the calculator's interface."""
        super(CalculatorApp, self).__init__(master)
        self._master = master
        self._master.title('Handmade Python Calculator')

        self._frames = {
            'first_frame': CalculatorFrame(self._master, pady=10, borderwidth=2),
            'second_frame': CalculatorFrame(self._master, padx=3),
            'third_frame': CalculatorFrame(self._master, padx=3),
            'fourth_frame': CalculatorFrame(self._master, padx=3),
            'fifth_frame': CalculatorFrame(self._master, padx=3),
            'sixth_frame': CalculatorFrame(self._master, padx=3)
        }
        self._display_box = CalculatorBox(self._frames['first_frame'], 2, 20)

        self._buttons = {
            'operators': {
                'divide_button': CalculatorButton(
                    self._frames['second_frame'],
                    text='/',
                    command=lambda: self._add_to_calculation_str('/')
                ),
                'multiply_button': CalculatorButton(
                    self._frames['third_frame'],
                    text='x',
                    command=lambda: self._add_to_calculation_str('*')
                ),
                'subtract_button': CalculatorButton(
                    self._frames['fourth_frame'],
                    text='-',
                    command=lambda: self._add_to_calculation_str('-')
                ),
                'add_button': CalculatorButton(
                    self._frames['fifth_frame'],
                    text='+',
                    command=lambda: self._add_to_calculation_str('+')
                ),
                'equal_button': CalculatorButton(
                    self._frames['sixth_frame'],
                    text='=',
                    command=lambda: self._display_result()
                ),
            },
            'numbers': {
                'zero_button': CalculatorButton(
                    self._frames['sixth_frame'],
                    text='1',
                    command=lambda: self._add_to_calculation_str('0')
                ),
                'one_button': CalculatorButton(
                    self._frames['fifth_frame'],
                    text='1',
                    command=lambda: self._add_to_calculation_str('1')
                ),
                'two_button': CalculatorButton(
                    self._frames['fifth_frame'],
                    text='2',
                    command=lambda: self._add_to_calculation_str('2')
                ),
                'three_button': CalculatorButton(
                    self._frames['fifth_frame'],
                    text='3',
                    command=lambda: self._add_to_calculation_str('3')
                ),
                'four_button': CalculatorButton(
                    self._frames['fourth_frame'],
                    text='4',
                    command=lambda: self._add_to_calculation_str('4')
                ),
                'five_button': CalculatorButton(
                    self._frames['fourth_frame'],
                    text='5',
                    command=lambda: self._add_to_calculation_str('5')
                ),
                'six_button': CalculatorButton(
                    self._frames['fourth_frame'],
                    text='6',
                    command=lambda: self._add_to_calculation_str('6')
                ),
                'seven_button': CalculatorButton(
                    self._frames['third_frame'],
                    text='7',
                    command=lambda: self._add_to_calculation_str('7')
                ),
                'eight_button': CalculatorButton(
                    self._frames['third_frame'],
                    text='8',
                    command=lambda: self._add_to_calculation_str('8')
                ),
                'nine_button': CalculatorButton(
                    self._frames['third_frame'],
                    text='9',
                    command=lambda: self._add_to_calculation_str('9')
                ),
            },
            'others': {
                'clear_button': CalculatorButton(
                    self._frames['second_frame'],
                    text='CLEAR',
                    command=lambda: self._clear_str()
                ),
                'decimal_button': CalculatorButton(
                    self._frames['sixth_frame'],
                    text='.',
                    command=lambda: self._add_to_calculation_str('.')
                )
            }
        }

        self._calculation_str = ''

    def _fill_calculator_window(self):
        """ Fills the GUI Calculator with widgets. """
        # First block
        self._display_box.configure(bg='light cyan', foreground='light sea green')
        self._display_box.pack(fill=tk.BOTH, expand=True)

        # Second block
        self._buttons['others']['clear_button'].place_button()
        self._buttons['others']['clear_button'].configure(fg='deep sky blue',
                                                          activeforeground='red')
        self._buttons['operators']['divide_button'].place_button()

        # Third block
        self._buttons['numbers']['seven_button'].place_button()
        self._buttons['numbers']['eight_button'].place_button()
        self._buttons['numbers']['nine_button'].place_button()
        self._buttons['operators']['multiply_button'].place_button()

        # Fourth block
        self._buttons['numbers']['four_button'].place_button()
        self._buttons['numbers']['five_button'].place_button()
        self._buttons['numbers']['six_button'].place_button()
        self._buttons['operators']['subtract_button'].place_button()

        # Fifth block
        self._buttons['numbers']['one_button'].place_button()
        self._buttons['numbers']['two_button'].place_button()
        self._buttons['numbers']['three_button'].place_button()
        self._buttons['operators']['add_button'].place_button()

        # Sixth block
        self._buttons['numbers']['zero_button'].place_button()
        self._buttons['others']['decimal_button'].place_button()
        self._buttons['operators']['equal_button'].place_button()
        self._buttons['operators']['equal_button'].configure(fg='firebrick1',
                                                             activeforeground='green')

        self._master.mainloop()

    def _clear_str(self):
        """ Clears the calculation string."""
        self._calculation_str = ''
        self._display_box.display_text(self._calculation_str)
        self._display_box.config(state='normal')

    def _add_to_calculation_str(self, char: str):
        """
        Adds the character corresponding to the button clicked to the calculation string.

        Args:
            char (str): character to add
        """
        self._calculation_str += char
        self._display_box.display_text(self._calculation_str)

    def _display_result(self):
        """ Displays the result of the calculation string."""
        self._display_box.display_text(Calculator(self._calculation_str)())
        self._display_box.config(state='disabled')

    def __call__(self):
        """ Creates the window for our GUI Calculator."""
        self._fill_calculator_window()
