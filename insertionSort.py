def insertionSort(theSeq):
    n = len(theSeq)
    #starts with the first item as the only sorted entry
    for i in range(1,n):#first item is sorted
        print(theSeq)
        value = theSeq[i]#save the value to be positioned
        #find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
            print(theSeq)
        theSeq[pos] = value
    return theSeq

if '__name__==__main__':
    lst=[5,4,3,2,1]
    print('Sorted List: ',insertionSort(lst))