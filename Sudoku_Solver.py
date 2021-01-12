def find_next_empty(puzzle):
    #finds empty cell in puzzle
    #return tuple row, col
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None # if all cells are filled 

def is_valid(puzzle, guess, row, col): 
    #checks if input is valid then returns true otherwise it returns false
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 
    col_vals = []
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals: 
        return False

    #Find which 3x3 box to run through
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True
    


def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #step1: Choose a cell in the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step1.1: validation check if all cells are filled
    if row is None:
        return True

    #step2: if a cell is empty input a value in range 1-9
    for guess in range(1,10): 
        #step2.1: check if guess is valid
        if is_valid(puzzle, guess, row, col):
            #place guess at the cell
            puzzle[row][col] = guess
            #step4: recursive call function
            if solve_sudoku(puzzle):
                return True

    #step5: if puzzle is not solved or guess doesnt solve puzzle then backtrack and try new number
    puzzle[row][col] = -1

    #step6: if none of the above work then puzzle is unsolvable 
    return False


if __name__ == '__main__':
    example_board = [
        [8, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)



            

