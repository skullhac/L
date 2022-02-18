def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        print(theSeq)
        smallNdx = i
        for j in range(i+1, n):#check if any element aftrer i contains smaller value
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

    return theSeq

def findNeg( intList ):
    n = len(intList)
    for i in range( n ) :
        if intList[i] < 0 :
            return i
    return None

if '__name__==__main__':
    lst=[7,6,5,4,3,2,1]
    print('Sorted List: ',selectionSort(lst))