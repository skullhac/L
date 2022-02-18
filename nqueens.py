from board import QueensBoard

def solveNQueens( board, col ):
   # A solution was found if n-queens have been placed on the board.
  if board.numQueens() == board.getsize() :
    return True
  else :
     # Find the next unguarded square within this column.  
    for row in range( board.getsize() ):
      if board.unguarded( row, col ):
        # Place a queen in that square. 
        board.placeQueen( row, col )        
        print( 'place queen at (', row, ', ', col, ')' )
        # Continue placing queens in the following columns.
        if solveNQueens( board, ( col + 1 ) % board.getsize() ) :
           # We are finished if a solution was found.
          return True
        else :
          # No solution was found with the queen in this square, so it
          # has to be removed from the board.
          board.removeQueen( row, col )
          print( 'remove queen at (', row, ', ', col, ')' )
      else:
          pass
          print(' b(', row, col, ') guarded ...')
     # If the loop terminates, no queen can be placed within this column.
    return False      

# def testNQueens(start_row, start_col):
#   print('test NQueens ...')
#   queensBoard = QueensBoard( 4 )
#   queensBoard.placeQueen( start_row, 0 )
#   if solveNQueens( queensBoard, start_col):
#     print( 'solved ...' )
#   else:
#     print( 'no solution ...' )
#
#   print( queensBoard )

#testNQueens(0, 1)   # no solution
#testNQueens(1, 1)   # solved
#testNQueens(2, 1)   # solved
#testNQueens(3, 1)   # no solution

if __name__=='__main__':
  start_row=3
  start_col=1
  queensBoard = QueensBoard(4)
  queensBoard.placeQueen( start_row, 0 )
  if solveNQueens( queensBoard, start_col):
    print( 'solved ...' )
  else:
    print( 'no solution ...' )