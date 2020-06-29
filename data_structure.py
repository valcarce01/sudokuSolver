class sudoku:
    """
    Own sudoku structure created by @Diego Valcarce to be able to analyze properly the values and get the solution
    """
    def __init__(self, sudoku, unknown = 0):
        """
        + sudoku: a sudoku like; must be an array of the values that has the own sudoku. Ordered by row/col
        + unknown: the parameter inclyed in the sudoku that has the meaning of unknown.
        """



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