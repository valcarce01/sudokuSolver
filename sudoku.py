"""
Created by:
    @Diego Valcarce
"""

import numpy as np
import pandas as pd

class sudoku:
    """
    Creates a sudoku. The size is 9x9, and the unknown numbers are identified as 0.
    + solved -> check if the sudoku is solved
    """

    def __init__(self, values):
        self._values = np.matrix(values)
        print(self._values)

    def solved(self):
        """
        Returns whether the sudoku is resolved. Need to:
        + 1. Verify all numbers are > 0 (other case is not completed)
        """
        # 1. > 0
        t = self._values.any(0)

    def mark(self):
        """
        Creates a list of options
        """


def sudoku_example():
    """
    Basic example of a sudoku just for working with
    """
    return [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if __name__ == "__main__":
    s = sudoku(sudoku_example())
    print(s.solved())