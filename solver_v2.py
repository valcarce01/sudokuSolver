"""
Tries to solve a sudoku
author: @Diego Valcarce
"""
import sudoku_v2
import time
import multiprocessing

class solver:
    def __init__(self, sudoku):
        """
        + sudoku: must be a sudoku_v2 object
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
        
        else:
            a = time.time()
            pos_solutions = self.force_resolve()
            print("Al posibilities generated in... {} seconds".format(time.time() - a))

            print("\n\nTrying all of them right now")
            pool = multiprocessing.Pool()
            a = time.time()
            sol = pool.map(func =self._check_list_solutions, iterable = pos_solutions)
            b = time.time()
            print(sol)
            print("Solutions checked in {} seconds".format(b - a))


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
        If not solved with the posibilities generated, tries to solve it by trying out all the possible combinations
        """
        sudoku = self.sudoku
        way = [[]]
        # What we will create is a list `way` which keeps all the possible ways
        for row_index in range(9):
            for col_index in range(9):
                val = sudoku.get_value((col_index, row_index))
                
                
                if isinstance(val, int):
                    val = [val]
                    
                # What we need to do is basiclly the cross product of all the options.
                # `extend` method
                
                if len(val) == 1:
                    for pos_sol in way:
                        pos_sol.extend(val)
                    
                else:
                    actual_way = way.copy()
                    
                    way = [self._flatten_([a, b]) for a in way for b in val]

        return way
                    
                    
    def _check_list_solutions(self, sudoku):
        """
        Converts list to sudoku object and checks if solution
        """
        s = sudoku_v2.sudoku(sudoku)
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
    s = solver(sudoku_v2.sudoku(sudoku_v2.example_sudoku()))

    peter_sudoku = \
        [
            8, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 3, 6, 0, 0, 0, 0, 0,
            0, 7, 0, 0, 9, 0, 2, 0, 0,
            0, 5, 0, 0, 0, 7, 0, 0, 0,
            0, 0, 0, 0, 4, 5, 7, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 3, 0,
            0, 0, 1, 0, 0, 0, 0, 6, 8,
            0, 0, 8, 5, 0, 0, 0, 1, 0,
            0, 9, 0, 0, 0, 0, 4, 0, 0
        ]
    s2 = solver(sudoku_v2.sudoku(peter_sudoku))
    s2.force_resolve()
    # for i in s2.sudoku._sudoku_values.items():
    #     print(i)
    # s.try_posibilities()