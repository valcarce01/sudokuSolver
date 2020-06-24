import time
def clean(sudoku):
    """
    Cleans the non-sense markers
    """
    print("Original:")
    for i in sudoku: print(i)

    print("\n\n")

    # First we will clean it up from left to right
    numbers_got_row = []
    for row_index in range(9):
        row = sudoku[row_index]
        print("row", row)

        # Once we got the complete row, if it's a list, it's a marker, not a number, so we got catch up the numbers
        for n in row:
            if not isinstance(n, list):
                numbers_got_row.append(n)
        print("got: ", numbers_got_row)
        
        # Once we know what numbers we got on a entire row, we can remove them from the markers
        cnt = 0
        for l in row:
            if isinstance(l, list):
                # remove with a while
                for number_to_remove in numbers_got_row:
                    while number_to_remove in l:
                        l.remove(number_to_remove)
                    
                # This point we have removed in l, but not in the original sudoku
                if len(l) == 1:
                    # We need to differenciate between we have only one option now, or many
                    sudoku[row_index][cnt] = l[0]
                else:
                    sudoku[row_index][cnt] = l
            
            cnt += 1
        # Reinitilyze the list
        numbers_got_row = []

    print("Rows working:")
    for i in sudoku: print(i)
    print("\n\n")
    
    # Next step, is to do exatly the same, but with columns.
    for col in range(9):              # From left to right
        # Create a list wich will hold up the values we got on a certain col
        numbers_got_col = []
        for row in range(9):          # Up-down
            if isinstance(sudoku[row][col], int):
                numbers_got_col.append(sudoku[row][col])

        # Same steps than before, check whether they are marks or actual numbers
        for row in range(9):
            l = sudoku[row][col]
            if isinstance(l, list):
                for number_to_remove in numbers_got_col:
                    while number_to_remove in l:
                        l.remove(number_to_remove)
                    
                    # This point we have removed in l, but not in the original sudoku
                    if len(l) == 1:
                        # We need to differenciate between we have only one option now, or many
                        sudoku[row][col] = l[0]
                    else:
                        sudoku[row][col] = l
    print("*" * 20)
    for i in sudoku: print(i)
    print("*" * 20)
    return sudoku



if __name__ == "__main__":
    
    su = [
        [5, 3, [1, 2, 4, 7], [2, 3, 4, 6, 8], 7, [2, 3, 4, 6, 8], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9]],
        [6, [1, 2, 4, 7], [1, 2, 4, 7], 1, 9, 5, [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9]],
        [[1, 2, 4, 7], 9, 8, [2, 3, 4, 6, 8], [2, 3, 4, 6, 8], [2, 3, 4, 6, 8], [1, 2, 3, 4, 5, 7, 8, 9], 6, [1, 2, 3, 4, 5, 7, 8, 9]],
        [8, [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], [1, 4, 5, 7, 9], 6, [1, 4, 5, 7, 9], [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], 3],
        [4, [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], 8, [1, 4, 5, 7, 9], 3, [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], 1],
        [7, [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], [1, 4, 5, 7, 9], 2, [1, 4, 5, 7, 9], [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], 6],
        [[1, 2, 3, 4, 5, 7, 8, 9], 6, [1, 2, 3, 4, 5, 7, 8, 9], [2, 3, 5, 6, 7], [2, 3, 5, 6, 7], [2, 3, 5, 6, 7], 2, 8, [1, 3, 4, 6]],
        [[1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], 4, 1, 9, [1, 3, 4, 6], [1, 3, 4, 6], 5],
        [[1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [2, 3, 5, 6, 7], 8, [2, 3, 5, 6, 7], [1, 3, 4, 6], 7, 9]
    ]
    a = time.time()
    print(clean(su))
    b = time.time()
    print(b - a)

    su2 =   [[5, 3, [1, 2, 4, 7], [2, 3, 4, 6, 8], 7, [2, 3, 4, 6, 8], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9]], 
            [6, [1, 2, 4, 7], [1, 2, 4, 7], 1, 9, 5, [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9]], 
            [[1, 2, 4, 7], 9, 8, [2, 3, 4, 6, 8], [2, 3, 4, 6, 8], [2, 3, 4, 6, 8], [1, 2, 3, 4, 5, 7, 8, 9], 6, [1, 2, 3, 4, 5, 7, 8, 9]], 
            [8, [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], [1, 4, 5, 7, 9], 6, [1, 4, 5, 7, 9], [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], 3], 
            [4, [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], 8, [1, 4, 5, 7, 9], 3, [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], 1], 
            [7, [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], [1, 4, 5, 7, 9], 2, [1, 4, 5, 7, 9], [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], 6], 
            [[1, 2, 3, 4, 5, 7, 8, 9], 6, [1, 2, 3, 4, 5, 7, 8, 9], [2, 3, 5, 6, 7], [2, 3, 5, 6, 7], [2, 3, 5, 6, 7], 2, 8, [1, 3, 4, 6]], 
            [[1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], 4, 1, 9, [1, 3, 4, 6], [1, 3, 4, 6], 5], 
            [[1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [2, 3, 5, 6, 7], 8, [2, 3, 5, 6, 7], [1, 3, 4, 6], 7, 9]]
    print(clean(su2))
