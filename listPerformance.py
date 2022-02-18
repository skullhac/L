from timeit import Timer
import matplotlib.pyplot as plt

def concatenation():
    l = []
    for i in range(1000):
        l = l + [i]

def append():
    l = []
    for i in range(1000):
        l.append(i)

def comprehension():
    l = [i for i in range(1000)]

def rangeFunction():
    l = list(range(1000))

t1 = Timer("concatenation()", "from __main__ import concatenation")
concatTime = t1.timeit(number=1000)
print("concatination ", concatTime, "milliseconds")
t2 = Timer("append()", "from __main__ import append")
appendTime = t2.timeit(number=1000)
print("append ", appendTime , "milliseconds")
t3 = Timer("comprehension()", "from __main__ import comprehension")
compTime= t3.timeit(number=1000)
print("comprehension ", compTime, "milliseconds")
t4 = Timer("rangeFunction()", "from __main__ import rangeFunction")
rangeTime = t4.timeit(number=1000)
print("list range ",rangeTime, "milliseconds")


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['concatination', 'append', 'comprehension', 'Range']
students = [concatTime,appendTime,compTime,rangeTime]
ax.bar(langs,students)
plt.show()