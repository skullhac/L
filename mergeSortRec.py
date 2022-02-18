from Chapter2.myarray import Array
def recMergeSort(theSeq, first, last, tmpArray):
    # Check the base case.
    newList=[]
    if first == last:
        return
    else:
        # Compute the mid point.
        mid = (first + last) // 2

        # Split the sequence and perform the recursive step.
        recMergeSort(theSeq, first, mid, tmpArray)
        recMergeSort(theSeq, mid + 1, last, tmpArray)

        # Merge the two ordered subsequences.
        mergeSeq(theSeq, first, mid + 1, last, tmpArray)
    return theSeq

# Merges the two sorted virtual subsequences: [left..right) [right..end)
# using the tmpArray for intermediate storage.

def mergeSeq( theSeq, left, right, end, tmpArray ):
    # Initialize two subsequence index variables.
    a = left
    b = right
    # Initialize an index variable for the resulting merged array.
    m = 0
    # Merge the two sequences together until one is empty.
    while a < right and b < end :
        if theSeq[a] < theSeq[b] :
            tmpArray[m] = theSeq[a]
            a += 1
        else :
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1

    # If the left subsequence contains more items append them to tmpArray.
    while a < right :
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1

    # Or if right subsequence contains more, append them to tmpArray.
    while b < end :
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1

    # Copy the sorted subsequence back into the original sequence structure.
    for i in range( end - left ) :
        theSeq[i+left] = tmpArray[i]
    return theSeq
# Sorts an array or list in ascending order using merge sort.
def mergeSort( theSeq ):
    n = len( theSeq )
    # Create a temporary array for use when merging subsequences.
    tmpArray = Array( n )
    # Call the private recursive merge sort function.
    recMergeSort( theSeq, 0, n-1, tmpArray )

theSeq = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(theSeq)