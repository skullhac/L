# Merges two sorted lists to create and return a new sorted list.
def mergeSortedLists(listA, listB):
# Create the new list and initialize the list markers.
    newList = list()
    a = 0
    b = 0

    # Merge the two lists together until one is empty.
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    # If listA contains more items, append them to newList.
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    # Or if listB contains more items, append them to newList.
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList

# listA=[1,2,3,4,5]
# listB=[5,6,7,8,9,10,11,12]
# print(mergeSortedLists(listA,listB))