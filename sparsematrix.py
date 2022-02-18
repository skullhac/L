# Implementation of the Sparse Matrix ADT using an array of linked lists.
from Chapter2.myarray import Array

class SparseMatrix :
    # Creates a sparse matrix of size numRows x numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._numCols = numCols
        self._listOfRows = Array( numRows )

     # Returns the number of rows in the matrix.
    def numRows( self ):
        return len( self._listOfRows )

     # Returns the number of columns in the matrix.
    def numCols( self ):
        return self._numCols

 # Returns the value of element (i,j): x[i,j]
    def __getitem__( self, ndxTuple ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next
        if curNode is not None and curNode.col == col:
            return curNode.value

     # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__( self, ndxTuple, value ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col :
            predNode = curNode
            curNode = curNode.next

        # See if the element is in the list.
        if curNode is not None and curNode.col == col :
            if value == 0.0 : # remove the node.
                if curNode == self._listOfRows[row] :
                    self._listOfRows[row] = curNode.next
                else :
                    predNode.next = curNode.next
            else : # change the node's value.
                curNode.value = value

        # Otherwise, the element is not in the list.
        elif value != 0.0 :
            newNode = _MatrixElementNode( col, value )
            newNode.next == curNode
            if curNode == self._listOfRows[row] :
                self._listOfRows[row] = newNode
            else :
                predNode.next = newNode

    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for row in range( self.numRows() ) :
            curNode = self._listOfRows[row]
            while curNode is not None :
                curNode.value *= scalar
                curNode = curNode.next

    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose( self ):
        newSparseMatrix = SparseMatrix(self.numCols(), self.numRows())
        for c in range(self.numCols()):
            for r in range(self.numRows()):
                newSparseMatrix[c, r] = self[r, c]
        return newSparseMatrix

    # Matrix addition: newMatrix = self + rhsMatrix.
    def __add__( self, rhsMatrix) :
        # Make sure the two matrices have the correct size.
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatable for adding."

        # Create a new sparse matrix of the same size.
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )

        # Add the elements of this matrix to the new matrix.
        for row in range( self.numRows() ) :
            curNode = self._listOfRows[row]
            while curNode is not None :
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        # Add the elements of the rhsMatrix to the new matrix.
        for row in range(rhsMatrix.numRows() ) :
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None :
                value = newMatrix[row, curNode.col]
                value += curNode.value
                newMatrix[row, curNode.col] = value
                curNode = curNode.next

        # Return the new matrix.
        return newMatrix

    # --- Matrix subtraction and multiplication ---
    def __sub__( self, rhsMatrix ) :
        # Make sure the two matrices have the correct size.
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatable for adding."

        # Create a new sparse matrix of the same size.
        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        # Add the elements of this matrix to the new matrix.
        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        # Add the elements of the rhsMatrix to the new matrix.
        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value -= curNode.value
                newMatrix[row, curNode.col] = value
                curNode = curNode.next

        # Return the new matrix.
        return newMatrix
    # def __mul__( self, rhsMatrix ) :

# Storage class for creating matrix element nodes.
class _MatrixElementNode :
    def __init__( self, col, value ) :
        self.col = col
        self.value = value
        self.next = None

smatrix = SparseMatrix(2,2)
s2matrix = SparseMatrix(2,2)
smatrix[0,0] = 1
smatrix[0,1] = 2
smatrix[1,0] = 3
smatrix[1,1] = 4

s2matrix[0,0] = 5
s2matrix[0,1] = 6
s2matrix[1,0] = 7
s2matrix[1,1] = 8



# print('value = ',smatrix[1,0])
# smatrix.scaleBy(10)
# print('scaled value = ',smatrix[1,0])

#addition 2 of Matrices
print('\n--------------------------------\n')
print('addition 2 of Matrices')
addmatrix = smatrix+s2matrix
for r in range(addmatrix.numRows()):
    print()
    for c in range(addmatrix.numCols()):
        tu = (r,c)
        print(addmatrix[r,c],end=' ')

#subtraction of  2 of Matrices
print('\n--------------------------------\n')
print('subtraction of  2 of Matrices')
addmatrix = s2matrix-smatrix
for r in range(addmatrix.numRows()):
    print()
    for c in range(addmatrix.numCols()):
        tu = (r,c)
        print(addmatrix[r,c],end=' ')

#Tranpose of Matrix
print('\n--------------------------------\n')
print('Transpose of Matrix')
Tsmatrix=smatrix.transpose()
for r in range(Tsmatrix.numRows()):
    print()
    for c in range(Tsmatrix.numCols()):
        tu = (r,c)
        print(Tsmatrix[r,c],end=' ')