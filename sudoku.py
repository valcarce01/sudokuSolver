"""
Created by:
    @Diego Valcarce
"""

import numpy as np

class sudoku:
    """
    Creates a sudoku
    """

    def __init__(self, values):
        self._values = np.matrix(values)
        print(self._values)

def sudoku_example():
    """
    Basic example of a sudoku just for working with
    """
    return [[], []]
