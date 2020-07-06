# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's,
# which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

def valid_solution(sudoku):
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # check each row
    validRow = [sorted(row) == correct for row in sudoku]
    # check each column
    validColumn = [sorted(column) == correct for column in zip(*sudoku)]
    # check block
    Block = []
    i = 0
    while i < 9:
        block = []
        block.extend([sudoku[i][0], sudoku[i][1], sudoku[i][2]])
        block.extend([sudoku[i + 1][0], sudoku[i + 1][1], sudoku[i + 1][2]])
        block.extend([sudoku[i + 2][0], sudoku[i + 2][1], sudoku[i + 2][2]])
        i += 3
        Block.append(block)
    i = 0
    while i < 9:
        block = []
        block.extend([sudoku[i][3], sudoku[i][4], sudoku[i][5]])
        block.extend([sudoku[i + 1][3], sudoku[i + 1][4], sudoku[i + 1][5]])
        block.extend([sudoku[i + 2][3], sudoku[i + 2][4], sudoku[i + 2][5]])
        i += 3
        Block.append(block)
    i = 0
    while i < 9:
        block = []
        block.extend([sudoku[i][6], sudoku[i][7], sudoku[i][8]])
        block.extend([sudoku[i + 1][6], sudoku[i + 1][7], sudoku[i + 1][8]])
        block.extend([sudoku[i + 2][6], sudoku[i + 2][7], sudoku[i + 2][8]])
        i += 3
        Block.append(block)

    validBlock = [sorted(block) == correct for block in Block]

    if validRow == validColumn == validBlock == [True, True, True, True, True, True, True, True, True]:
        return(True)
    else:
        return(False)

# I know, my code for checking blocks is really long.
# zip(*sudoku) is really amazing

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 0, 3, 4, 8],
                          [1, 0, 0, 3, 4, 2, 5, 6, 0],
                          [8, 5, 9, 7, 6, 1, 0, 2, 0],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 0, 1, 5, 3, 7, 2, 1, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
