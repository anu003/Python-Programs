# -*- coding: utf-8 -*-
import itertools
import math
class Sudoku(object):
    #your code here
    def __init__(self, inputsudoku):
        self.inputsudoku = inputsudoku

    def is_valid(self):
        pass
        len_sudoku = len(self.inputsudoku)
        subsquare = math.sqrt(len_sudoku)
        squares = []

        # Validating if not boolean
        if isinstance(self.inputsudoku[0][0], bool):
            return False
        
        # Validating Data structure dimension: NxN where N > 0 and √N == integer
 
        if int(subsquare) == subsquare:
            for row in self.inputsudoku:
                # validating the numbers in a row
                if len(row) != len_sudoku or set(row) != set(range(1,len_sudoku+1)):
                    return False

            inv_sudoku = [list(i) for i in zip(*self.inputsudoku)]

            for inv_row in inv_sudoku:
                # validating the numbers in a column
                if len(inv_row) != len_sudoku or set(inv_row) != set(range(1,len_sudoku+1)):
                    return False

            #validating subsquares
            for i in range(0, len_sudoku, int(subsquare)):
                for j in range(0, len_sudoku,int(subsquare)):
                    square = list(itertools.chain(row[j:j+int(subsquare)] for row in self.inputsudoku[i:i+ int(subsquare)]))
                    squares.append(square)
    
            for row in squares:
                test = []
                for sub_row in row:
                    test += sub_row
                if set(test) != set(range(1, len_sudoku+1)):
                    return False
            
            return True



##import math
##
##class Sudoku(object):
##    def __init__(self, board):
##        self.board = board
##        
##    def is_valid(self):
##        if not isinstance(self.board, list):
##            return False
##        n = len(self.board)
##        rootN = int(round(math.sqrt(n)))
##        if rootN * rootN != n:
##            return False
##        isValidRow = lambda r : (isinstance(r, list) and
##                                 len(r) == n and
##                                 all(map(lambda x : type(x) == int, r)))
##        if not all(map(isValidRow, self.board)):
##            return False
##        oneToN = set(range(1, n + 1))
##        isOneToN = lambda l : set(l) == oneToN
##        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
##        squares = [[self.board[p+x][q+y] for x in range(rootN) 
##                                         for y in range(rootN)] 
##                                         for p in range(0, n, rootN)
##                                         for q in range(0, n, rootN)] 
##        return (all(map(isOneToN, self.board)) and
##                all(map(isOneToN, tranpose)) and
##                all(map(isOneToN, squares)))

        
s = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8], 
  [1,9,5, 2,8,7, 6,3,4]])

p = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

q = Sudoku([[True]])
print q.is_valid()
