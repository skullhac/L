import numpy as np
def positionIdentifier(list_size,value_searched):
    lst=list(range(list_size))
    np.random.shuffle(lst)
    for i in range(list_size):
        if(value_searched==lst[i]):
            return i+1
    return None
def simulator(n):
    lst=[0]*n
    for i in range(n):
        lst[i]=positionIdentifier(1000,50)
    worst_case=max(lst)
    best_case=min(lst)
    average_case=sum(lst)/n
    print("Best case: Minimum comparisons lead to specified value = ",best_case)
    print("Average case: Average comparisons lead to specified value = " , average_case)
    print("Worst case: Maximum comparisons lead to specified value =  " , worst_case)

simulator(100)

