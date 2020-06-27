""""
by: @Diego Valcarce

class sudoku:
    + add a number
    + mark as possible answer
"""
import numpy as np
import time
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
        self._unknown_parameter = unknown
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
        pos = self._sudoku_table[position[1]][position[0]]
        # Check wheter it's an actual value or not
        if (isinstance(self._sudoku_values[pos], list) or self._sudoku_values[pos] == self._unknown_parameter):
            self._sudoku_values[pos] = value
        else:
            raise AlreadyOnTable("There's already a value on that position")


    def add_marker(self, mark, position):
        """
        Adds a mark of possible answers on a certain positions of the sudoku
        + Position must be a tuple like: (5, 2), where 5 is the column and 2 the row.
        """
        self._sudoku_values[self._sudoku_table[position[1]][position[0]]] = [*mark] if (isinstance(mark, tuple) or isinstance(mark, list)) else [mark]

    def get_value(self, position):
        """
        Return the value of a position
        """
        return self._sudoku_values[self._sudoku_table[position[1]][position[0]]]
    
    def get_value_by_name(self, name):
        """
        Returns the value of a given position, like A1, A2...
        """
        return self._sudoku_values[name]

    def get_row(self, index):
        """
        Returns the whole row given an index
        """
        return [self._sudoku_values[n] for n in self._sudoku_table[index]]

    def get_column(self, index):
        """
        Returns a whole column
        """
        return [self._sudoku_values[n] for n in self._sudoku_table[:,index]]

    def get_block(self, block):
        """
        Returns block. Distributed like:
        ____________________
         0  |   1   |   2
         ___|_______|_______
            |       |
         3  |   4   |    ....
        
        will return the values in order, like:
        block 1: A1 A2 A3 B1 B2 B3 C1 C2 C3...
        """
        # The up/down will be deffined by entire division (//)
        # The right/left by the module (%)
        up = (block) // 3 * 3
        left = (block) % 3 * 3

        # Now create the return
        # First step is to get the indexes for the dictionary
        return_list = []
        for row in self._sudoku_table[up : up + 3, left : left + 3]:
            for index in row:
                return_list.append(self._sudoku_values[index])

        return return_list
    
    def get_block_combinations(self):
        """
        Returns a list of combinations of the letters (A1, A2...) for each block
        """
        return_list = []
        for block in range(9):
            up = (block) // 3 * 3
            left = (block) % 3 * 3
            aux = []
            for row in self._sudoku_table[up : up + 3, left : left + 3]:
                
                for index in row:
                    aux.append(index)
                if aux not in return_list:
                    return_list.append(aux)

        return return_list


    def get_block_index(self, block):
        """
        Returns a list of the indexes of the actual block
        """
        up = (block) // 3 * 3
        left = (block) % 3 * 3
        return_list = []
        for row in self._sudoku_table[up : up + 3, left : left + 3]:
            for index in row:
                return_list.append(index)

        return return_list

    def check_win(self):
        """
        Check if it's solved
        """
        # We need to call the _check_win_unique and after that, check the boxes
        result = []
        for index in range(9):
            result.append(self._check_win_unique_(self.get_column(index)))
            result.append(self._check_win_unique_(self.get_row(index)))
            result.append(self._check_win_unique_(self.get_block(index)))
        set_result = set(result)
        # If all are OKs, the len should be 1, 'cause it will be all True:
        if len(set_result) != 1:
            return False
        
        # So, if it's of len 1, we need to check if it's a False or True
        for element in iter(set_result):
            if element:
                return True
            else:
                return False
        

    def _check_win_unique_(self, to_check):
        """
        Given a list of values, checks if are all different in the same list. So can be an actual solution.
        """
        try:  
            return len(set(to_check)) == 9
        except TypeError:       # If a list
            return False

def example_sudoku():
    return [5, 3, 0, 0, 7, 0, 0, 0, 0,
        6, 0, 0, 1, 9, 5, 0, 0, 0,
        0, 9, 8, 0, 0, 0, 0, 6, 0,
        8, 0, 0, 0, 6, 0, 0, 0, 3,
        4, 0, 0, 8, 0, 3, 0, 0, 1,
        7, 0, 0, 0, 2, 0, 0, 0, 6,
        0, 6, 0, 0, 0, 0, 2, 8, 0,
        0, 0, 0, 4, 1, 9, 0, 0, 5,
        0, 0, 0, 0, 8, 0, 0, 7, 9]

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
    