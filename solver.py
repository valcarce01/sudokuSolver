"""
Tries to solve a sudoku
author: @Diego Valcarce
"""
import sudoku
import time
import multiprocessing
from graph import Graph
import numpy as np

class solver:
    def __init__(self, sudoku):
        """
        + sudoku: must be a sudoku object
        """
        self.sudoku = sudoku
        added_numbers = self.generate_posibilities(self.sudoku)
        
        a = time.time()
        while (added_numbers + self.generate_posibilities(self.sudoku)) > added_numbers:
            added_numbers += self.generate_posibilities(self.sudoku)
        print("All we can do working with columns and rows done in: ", time.time() - a)

        # Check win
        if self.sudoku.check_win():
            print("Win")
        
       

    def generate_posibilities(self, sudoku):
        """
        Creates all the posibilities
        """
        # We'll create a counter to know how long we can handle to be executing the function (as long as the cnt increases)
        added_numbers = 0

        possibilities = set(range(1, 10))
        for row_index in range(9):
            # Let's see what numbers we got
            row = set([item for item in sudoku.get_row(row_index) if not isinstance(item, list)])
            for col_index in range(9):
                # We just need to get the value if we want to mark it (AKA we don't actually know the rial value)
                if sudoku.get_value((col_index, row_index)) == 0 or isinstance(sudoku.get_value((col_index, row_index)), list):
                    # The column we are studying:
                    col = set([item for item in sudoku.get_column(col_index) if not isinstance(item, list)])
                    # On each position we can use the values in `posibilities` that are not in
                    # the union of what we got on col + row
                    all_row_col = row.union(col)
                    pos = possibilities.difference(all_row_col)

                    # We also need to remove the already in the block
                    actual_block = self._get_block_((row_index, col_index))
                    values_block = [item for item in sudoku.get_block(actual_block) if not isinstance(item, list)]

                    # And remove them:
                    pos_list = list(pos.difference(values_block))

                    # Then, add them to the sudoku. But before, we need to check if the len is 1, because
                    # that will mean that in that position, that value is the only one that can be setted
                    if len(pos_list) == 1:
                        sudoku.add_value(pos_list[0], (col_index, row_index))
                        added_numbers += 1

                    else:
                        sudoku.add_marker(pos_list, (col_index, row_index))
        return added_numbers
        
        
    def force_resolve(self):
        """
        If not solved with the posibilities generated, tries to solve it by trying out all the possible combinations, using for that, graphs.
        """
        graph = Graph()
        vertices = [chr(letter) + str(number) for letter in range(65, 74) for number in range(1, 10)]
        for cell in vertices:
            graph.add_vertex(cell)

        # We load the numpy array:
        table = self.sudoku._sudoku_table

        for index in range(9):
            row = table[index]
            col = table[:, index]
            combinations_row = [(a, b) for a in row for b in row if a != b and b != a]
            combinations_col = [(a, b) for a in col for b in col if a != b and b != a]
            # And create the combinations as edges on the graph
            for edge_index in range(len(combinations_row)):
                graph.add_edge(*combinations_row[edge_index])
                graph.add_edge(*combinations_col[edge_index])

        
        block = self.sudoku.get_block_combinations()
        for block_values in block:
            combinations = [(a, b) for a in block_values for b in block_values if a != b and b != a]
            for edge in combinations:
                graph.add_edge(*edge)
        
        # Now we start calculating
        



                    
                    
    def _check_list_solutions(self, sudoku):
        """
        Converts list to sudoku object and checks if solution
        """
        s = sudoku.sudoku(sudoku)
        return s.check_win()
                      
    def _flatten_(self, nested_list):
        flat_list = []
        for elem in nested_list:
            if isinstance(elem, list):
                flat_list.extend(self._flatten_(elem))
            
            else:
                flat_list.append(elem)
        
        return flat_list      
    
    def _get_block_(self, index: tuple):
        """
        Returns the block number that correponds to an index (like tuple) like (5, 2), being 5 the rows, and 2 the cols.
        """
        start = 0

        col, row = index[0], index[1]

        # The objective is to get a number 0-8 of block, as we know the limits of them, we can just add value in rows each 1 and
        # in cols each 3

        if 3 <= col < 6:
            start += 3
        elif col >= 6:
            start += 6
        
        if 3 <= row < 6:
            start += 1
        elif row >= 6:
            start += 2

        return start


if __name__ == "__main__":
    s = solver(sudoku.sudoku(sudoku.example_sudoku()))
    s.force_resolve()

    # peter_sudoku = \
    #     [
    #         8, 0, 0, 0, 0, 0, 0, 0, 0,
    #         0, 0, 3, 6, 0, 0, 0, 0, 0,
    #         0, 7, 0, 0, 9, 0, 2, 0, 0,
    #         0, 5, 0, 0, 0, 7, 0, 0, 0,
    #         0, 0, 0, 0, 4, 5, 7, 0, 0,
    #         0, 0, 0, 1, 0, 0, 0, 3, 0,
    #         0, 0, 1, 0, 0, 0, 0, 6, 8,
    #         0, 0, 8, 5, 0, 0, 0, 1, 0,
    #         0, 9, 0, 0, 0, 0, 4, 0, 0
    #     ]
    # s2 = solver(sudoku.sudoku(peter_sudoku))
    # s2.force_resolve()
    # for i in s2.sudoku._sudoku_values.items():
    #     print(i)
    # s.try_posibilities()