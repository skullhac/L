from my_array_list import Array2D

class QueensBoard:
    def __init__( self, n ):
        """Create an nxn empty borad"""
        self.size = n
        self._board = Array2D( n, n )
        self.QUEEN = 'Q'
        self.NON_QUEEN = 'x'
        self.reset()

    def __str__( self ):
        s = '+'
        for l in range( self.size ):
            s += '-'
        s += '+\n'    # top bound
        for row in range( self.size ):
            s += '|'
            for col in range( self.size ):
                s += self._board[ row, col ]
            s += '|\n'
        # bottom bound
        s += '+'
        for l in range( self.size ):
            s += '-'
        s += '+\n'   
        return s


    def getsize( self ):
        """Return the size of the board"""
        return self.size

    def numQueens( self ):
        """Return the number queens currently positioned on the board"""
        count = 0
        for row in range( self.size ):
            for col in range( self.size ):
                if self._board[ row, col ] == self.QUEEN:
                    count += 1
        return count

    def unguarded( self, row, col ):
        """Return if the current location is unguarded"""
        return self._rowUngarded( row ) and self._colUngarded( col ) \
            and self._upLeftDownRightUnguard( row, col ) \
            and self._upRightDownLeftUnguard( row, col )

    def _rowUngarded( self, row ):
        """Return if the current row is unguarded"""
        for col in range( self.size ):
            if self._board[ row, col ] == self.QUEEN:
                return False
        return True
        
    def _colUngarded( self, col ):
        """Return if the current column is unguarded"""
        for row in range( self.size ):
            if self._board[ row, col ] == self.QUEEN:
                return False
        return True
        
    def _upLeftDownRightUnguard( self, row, col ):
        """Return if the up left to low right diagonal is unguarded"""
        # first moving up
        r = row
        c = col
        while r >= 0 and c >= 0:
            if self._board[ r, c ] == self.QUEEN:
                return False
            r -= 1
            c -= 1
        # now moving down
        r = row
        c = col
        while r < self.size and c < self.size:
            if self._board[ r, c ] == self.QUEEN:
                return False
            r += 1
            c += 1
        # if we reach here, no QUEEN is in sight
        return True

    def _upRightDownLeftUnguard( self, row, col ):
        """Return if the up right to low left diagonal is unguarded"""
        # first moving up
        r = row
        c = col
        while r >= 0 and c < self.size:
            if self._board[ r, c ] == self.QUEEN:
                return False
            r -= 1
            c += 1
        # now moving down
        r = row
        c = col
        while r < self.size and c >= 0:
            if self._board[ r, c ] == self.QUEEN:
                return False
            r += 1
            c -= 1
        # if we reach here, no QUEEN is in sight
        return True

    def placeQueen( self, row, col ):
        """Place the queen at board[row, col]"""
        self._board[ row, col ] = self.QUEEN

    def removeQueen( self, row, col ):
        """Remove the queen at board[row, col]"""
        self._board[ row, col ] = self.NON_QUEEN

    def reset( self ):
        """ Reset the board """
        for row in range( self.size ):
            for col in range( self.size ):
                self._board[ row, col ] = self.NON_QUEEN

    def draw( self ):
        """Draw the text represntation of the grid"""
        print( self )

