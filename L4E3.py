from matplotlib import pyplot as plt
import numpy as np

def ex1( n ):#Function with execution time of O(n)
    total = 0
    for i in range( n ) :
        total += i
    return total

def ex2( n ):#Function with execution time of O(n)
    count = 0
    for i in range( n ) :
        count += 1
    for j in range( n ) :
        count += 1
    return count

def ex3( n ):#Function with execution time of O(n)
    count = 0
    for i in range( n ) :
        for j in range( n ) :
            count += 1
    return count

def ex4( n ): #Function with execution time of O(n)
    count = 0
    for i in range( n ) :
        for j in range( 25 ) :
            count += 1
    return count

def ex5( n ):#Function with execution time of O(n^2)
    count = 0
    for i in range( n ) :
        for j in range( i+1 ) :
            count += 1
    return count

def ex6( n ):#Function with execution time of O(log(n))
    count = 0
    i = n
    while i >= 1 :
        count += 1
        i = i // 2
    return count

def ex7( n ): #Function with execution time of O(nlog(n))
    count = 0
    for i in range( n ):
        count += ex6( n )
    return count

def simumlator(n):
    Steps_ex1=[0]*n
    Steps_ex2 = [0] * n
    Steps_ex3 = [0] * n
    Steps_ex4 = [0] * n
    Steps_ex5 = [0] * n
    Steps_ex6 = [0] * n
    Steps_ex7 = [0] * n
    for i in range(n):
        Steps_ex1[i]=ex1(i)
        Steps_ex2[i]=ex2(i)
        Steps_ex3[i]=ex3(i)
        Steps_ex4[i]=ex4(i)
        Steps_ex5[i]=ex5(i)
        Steps_ex6[i]=ex6(i)
        Steps_ex7[i]=ex7(i)
    x = list(range(n))
    plt.plot(x, Steps_ex1)
    plt.plot(x, Steps_ex2)
    plt.plot(x, Steps_ex3)
    plt.plot(x, Steps_ex4)
    plt.plot(x, Steps_ex5)
    plt.plot(x, Steps_ex6)
    plt.plot(x, Steps_ex7)
    plt.grid(which='both')
    plt.xlabel('Input Size(n)')
    plt.ylabel('Number of Statements Executed')
    plt.legend(['ex1 with [T(n) = n * 1]','ex2 with T(n) = 2n','ex3 with [T(n) = n * n]','ex4 with [T(n) = 25n]','ex5 with [T(n) = n (n+1)/2]','ex6 with [T(n) =  log(n)]','ex7 with [T(n) = nlog(n)]'])
    plt.show()
simumlator(150)
