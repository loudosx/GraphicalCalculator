"""
@Author: Lou DOS
@Date: 2023-03-18
@Last modified by: Lou DOS
@Last modified at: 2023-03-18 15:05:17
@Purpose: useful methods to implement the calculator's backend.
"""
def invert_dic(dic: dict):
    inverted_dict = dict()
    for key, value in dic.items():
        inverted_dict.setdefault(value, list()).append(key)

    return inverted_dict
