import numpy as np
import time

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]== -1:
                return r,c

    return None,None

def check_guess(puzzle,g,r,c):
    for k in puzzle[r]:
        if g==k:
            return False

    for i in range(9):
        if puzzle[i][c]==g:
            return False

    rb= (r//3)*3
    cb= (c//3)*3
    for i in range(rb, rb+3):
       for j in range(cb,cb+3):
           if puzzle[i][j]==g:
               return False

    return True

def solve_sudoku(puzzle):
    r,c= find_next_empty(puzzle)
    if r is None:
        return True

    for g in range(1,10):
      if check_guess(puzzle,g,r,c):
          puzzle[r][c]=g
          time.sleep(0.5)
          print(np.array(puzzle))
          print("\n\n")
          if  solve_sudoku(puzzle):
               return True

          puzzle[r][c]=-1


    return False



example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
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
print(np.array(example_board))
