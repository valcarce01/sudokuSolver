from graph import Graph

class Solver:
    def __init__(self, sudoku: list):
        """Solves the sudoku (tries to)"""
        self.graph = Graph()
        self.sudoku = Sudoku(sudoku)

    def check_unique(self):
        """
        Can be some cases where one cell can hold more than one value, however this value
        is in the unique position it can be put
        """
        # First we need to check by rows
        for i in range(81):
            # Now calculate the elements in its row
            pos_x = i // 9; pos_y = i % 9; pos = 9 * pos_x + pos_y
            row = range(i // 9 * 9, i // 9 * 9 + 9)
            col = list(range(i % 9, 81, 9))
            start_row = i // 9 // 3 * 3
            start_col = i % 9 // 3 * 3
            start_block_i = start_row * 9 + start_col
            block = [i for i in range(start_block_i, start_block_i + 3)] +\
                [i for i in range(start_block_i + 9, start_block_i + 12)] +\
                [i for i in range(start_block_i + 18, start_block_i + 21)]

            values = self.sudoku[i]
            print(values)
            if len(values) != 1:
                # wont have same to check for len 1 because of this will be authomcaticly
                # removed
                for v in values:
                    # now we check for each of the values
                    aux_bool = False
                    print(block)
                    print(pos); print("\n")
                    for r in block:
                        if r != pos:
                            print(v in self.sudoku[r], self.sudoku[r], v)
                            aux_bool = aux_bool or v in self.sudoku[r] # but not the actual cell
                    print(aux_bool)
                    
            if i == 3:
                break
            
        

    def graph_solve(self):
        """Solves the coloring problem"""
        removed_values = 0;  continue_ = True
        while continue_:
            for i in range(81):
                values = self.sudoku[i]
                if len(values) == 1:
                    points_to = self.graph[i]
                    for to_check in points_to:
                        if to_check != i:
                            removed_values += self.sudoku.__delitem__((to_check, values[0]))
            print(removed_values)
            continue_ = removed_values > 0
            removed_values = 0
        print(self.sudoku)
    
    def pairs(self):
        """Applys pairs tecnichs for solving sudokus"""

    
    


class Sudoku:
    """Sudoku object to ez work from other classes
    + sudoku: list of all the values in order by row
    + unknown_param: the symbol used as not known value"""
    def __init__(self, sudoku: list, unkown_param = 0):
        """"""
        self.values = dict()
        for idx in range(81):
            actual_value = sudoku[idx]
            if actual_value in range(1, 10):
                self.values[str(idx)] = [actual_value]
            elif actual_value == unkown_param:
                self.values[str(idx)] = list(range(1, 10))

    def __delitem__(self, to_delete: tuple):
        """Pruebas"""
        index, value = to_delete[0], to_delete[1]
        where = self.values[str(index)]
        if len(where) == 1 and value == where[0]:
            print(where, index, value)
            raise Exception("Not an option, crack")
        try:
            where.remove(value)
            return 1
        except ValueError:
            return 0

    def __getitem__(self, target: int):
        """Returns a list of the values that makes sense for the target position"""
        return self.values[str(target)]
    
    def __str__(self):
        """Prints it"""
        to_print = str()
        for i in range(81):
            if (i % 9 == 0):
                to_print += "\n"
            to_print += str(self.values[str(i)])
        return to_print
            

if __name__ == "__main__":
    
    sudoku =   [4, 6, 0, 0, 9, 0, 0, 0, 0,
                0, 5, 2, 1, 0, 0, 0, 9, 0,
                0, 0, 0, 2, 3, 0, 5, 0, 0,
                8, 0, 0, 0, 0, 0, 0, 0, 7,
                0, 0, 0, 0, 2, 0, 0, 0, 8,
                3, 0, 0, 0, 0, 0, 0, 0, 9,
                0, 0, 0, 5, 1, 0, 8, 0, 0,
                0, 7, 8, 6, 0, 0, 0, 2, 0,
                6, 1, 0, 0, 8, 0, 0, 0, 0]
    Sudo = Sudoku(sudoku)
    s = Solver(sudoku)
    print(Sudo)
    s.graph_solve()
    s.check_unique()
