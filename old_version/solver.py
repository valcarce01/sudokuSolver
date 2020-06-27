"""
The way this will work is by creating all the posibilities that are posible and then try them out.

#### IDEAS #########
+ One way to improve the time spent, on the _posibilities_maker_ is to run it on a multiprocess nistead of on
a loop, as long as it's independent for each block.
"""
import sudoku
import time
import solver_clean_posibilities

class solver:
    """
    Solves, if posible, a sudoku given as a numpy matrix
    """
    def __init__(self, s, unknown = 0):
        """
        + s -> sudoku, numpy matrix like
        + unknown -> how unknown parameters are identified, by default '0'
        """
        # What we will do is to change the unknown parameters for the posibilities it can have.
        # We will time how long does it take to mark all the possibilities
        time_start = time.time()
        self.sudoku = self._posibilities_marker_(s, unknown)
        time_end = time.time()
        print("Possibilities made in: ", time_end - time_start)

        # Next step is to clean up all the generated solutions, as long as it's not possible to
        # get the same 2 numbers (or more) in the same row or column. 
        self.sudoku_clean = self._clean_posibilities_(self.sudoku)
        

    
    def _posibilities_marker_(self, s, unknown):
        """
        Returns a sudoku like, but arrays of the posibilities where were unknown parameters before.
        """
        # First step would be to know the posible numbers each block (3x3) can handle.
        for start, end in [[0, 3], [3, 6], [6, 9]]: # We move right on the sudoku
            numbers_got = []
            for row in range(9):                    # We move down
                numbers_got += [n for n in s[row][start:end]] # This way we create a list of the numbers we got on each block (3x3)
                # We remove the unknown value, while we don't actually want it
                while unknown in numbers_got:
                    numbers_got.remove(unknown)
                
                if (row + 1) % 3 == 0:
                    # We will get here when we loop the entire array, so we can actually try to get the numbers are missing
                    subtract = [item for item in range(1, 10) if item not in numbers_got]
                    # subtract now has the number each block (in order) is missing
                    # So now, where in the original sudoku was a unknown (from now we'll be talking about a 0 as it's the default
                    # one)
                    # We need to travel around the blocks again, but now no on every one.
                    
                    # When the if is executed, means we are at the end of the block, so we know where it's ended, and, as long as we
                    # actually know the size of the block too, it's posible to execute it only in the block we want (reducing so
                    # much the executing time).
                    for block_row in range(row - 2, row + 1):
                        for index in range(start, end):
                            if s[block_row][index] == 0:
                                # We sustitute the unknown value with the list of values that it actually can have.
                                s[block_row][index] = subtract                                 
                    # When we got'em, we can reboot the array
                    numbers_got = []
        return s

        
    def _clean_posibilities_(self, sudoku):
        """
        Removes the options that doesn't make sense because of be in the same column/row
        """
        return solver_clean_posibilities.clean(sudoku)

        


if __name__ == "__main__":
    s = sudoku.sudoku_example()
    for i in s:
        print(i)
    sudo = solver(s)