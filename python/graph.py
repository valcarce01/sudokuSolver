import numpy as np
from functools import reduce # to use a 2 argument function with 3 values

class Graph():
    """Implementation of a simple undirected graph for solving sudokus"""
    def __init__(self, sudoku: list):
        """Save the data"""
        self._sudoku = sudoku
        self._create_adjacency_matrix()

    def _create_adjacency_matrix(self):
        """Creates the adjacency matrix for the sudoku"""
        self.adjacency = np.zeros(shape=(81, 81), dtype=bool)
        for i in range(81):
            # Now calculate the elements in its row
            row = list(range(i // 9 * 9, i // 9 * 9 + 9))
            # The ones on the column
            col = list(range(i % 9, 81, 9))
            
            # Now the block
            start_row = i // 9 // 3 * 3
            start_col = i % 9 // 3 * 3
            start_block_i = start_row * 9 + start_col
            block = [i for i in range(start_block_i, start_block_i + 3)] +\
                [i for i in range(start_block_i + 9, start_block_i + 12)] +\
                [i for i in range(start_block_i + 18, start_block_i + 21)]
            # Its more efficcient to make the union between them and then just one loop
            union = reduce(np.union1d, (row, col, block))
            # Now introduce the condition into the adjacency matrix
            for to_add in union:
                self.adjacency[i, to_add] = True
    
    
    def __getitem__(self, tarjet: int):
        """Returns the np.array of the items the target is pointing to"""
        return np.where(self.adjacency[tarjet] == True)[0]
        
        


if __name__ == "__main__":
    g = Graph([])
    print(g[1])