# Sorts a sequence of positive integers using the radix sort algorithm.

from Chapter8.llistqueue import Queue
from Chapter2.myarray import Array
import math


class Radix():


    def numOfDigits(n):
        if n > 0:
            digits = int(math.log10(n))+1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-n))+2 # +1 if you don't count the '-'
        return digits

    def radixSort( intList, numDigits ):
        # Create an array of queues to represent the bins.
        binArray = Array( 10 )
        for k in range( 10 ):
            binArray[k] = Queue()

        # The value of the current column.
        column = 1

        # Iterate over the number of digits in the largest value.
        for d in range( numDigits ):
        # Distribute the keys across the 10 bins.
            for key in intList :
                digit = (key // column) % 10
                binArray[digit].enqueue( key )

            # Gather the keys from the bins and place them back in intList.
            i = 0
            for bin in binArray :
                while not bin.isEmpty() :
                    intList[i] = bin.dequeue()
                    i += 1

            # Advance to the next column value.
            column *= 10
        return intList