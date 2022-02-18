# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1):
        # Bubble the largest item to the end.
        for j in range(n - 1-i):
            if theSeq[j] > theSeq[j + 1]: # swap the j and j+1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq
if '__name__==__name__':
    Seq=[5,3,9,1,8,10,2]
    sortedList=bubbleSort(Seq)
    print(sortedList)