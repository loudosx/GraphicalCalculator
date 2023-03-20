"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-19 22:16:15
"""
# IMPORT: GUI library
import tkinter as tk

# IMPORT: Graphic Calculator
from src.calculator_interface.calculator_app import CalculatorApp

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('300x500')
    CalculatorApp(window)()
