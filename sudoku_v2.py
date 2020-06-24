""""
by: @Diego Valcarce

class sudoku:
    + add a number
    + mark as possible answer
"""
import numpy as np
##############
# Exceptions:
class AlreadyOnTable(Exception):
    """
    Raised when trying to set a value that it´s already set.
    """
    pass

##############

class sudoku:
    """
    Will be stored as a pair of a matrix implemented in numpy and a dictionary (hash table) wich actually has
    the values.
    """
    def __init__(self, values, unknown = 0):
        """
        + values: set of values of the sudoku, all in the same input.
        + unknown: parameter that identifies the unknown values.
        """
        # Create the table wi will play with:
        self._sudoku_table = np.array([[chr(letter) + str(number) for number in range(1, 10)] for letter in range(65, 74)])
        # Create the dictionary that will store the rial data:
        self._sudoku_values = dict(zip([chr(letter) + str(number) for letter in range(65, 74) for number in range(1, 10)], values))

        print(self._sudoku_table, "\n\n", self._sudoku_values)

    def add_value(self, value, position):
        """
        Add a value in a certain position of the sudoku.
        + Position must be a tuple like: (5, 2), where 5 is the column and 2 the row.
        """


    def add_marker(self, mark, position):
        """
        Adds a mark of possible answers on a certain positions of the sudoku
        + Position must be a tuple like: (5, 2), where 5 is the column and 2 the row.
        """

    def get_value(self, position):
        """
        Return the value of a position
        """
        return self._sudoku_values[self._sudoku_table[position[1]][position[0]]]

    def get_row(self, index):
        """
        Returns the whole row given an index
        """
        return [s._sudoku_values[n] for n in s._sudoku_table[index]]

    def get_column(self, index):
        """
        Returns a whole column
        """
        return [s._sudoku_values[n] for n in s._sudoku_table[:,index]]

if __name__ == "__main__":
    s = sudoku(
        [5, 3, 0, 0, 7, 0, 0, 0, 0,
        6, 0, 0, 1, 9, 5, 0, 0, 0,
        0, 9, 8, 0, 0, 0, 0, 6, 0,
        8, 0, 0, 0, 6, 0, 0, 0, 3,
        4, 0, 0, 8, 0, 3, 0, 0, 1,
        7, 0, 0, 0, 2, 0, 0, 0, 6,
        0, 6, 0, 0, 0, 0, 2, 8, 0,
        0, 0, 0, 4, 1, 9, 0, 0, 5,
        0, 0, 0, 0, 8, 0, 0, 7, 9]
    )