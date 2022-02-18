from radixsort import Radix

def main():
    radixsort = Radix()
    list = [23,10,18,51,5,13,31,54,48,62,29,8,37]
    numdig= Radix.numOfDigits(max(list))
    sortedList =Radix.radixSort(list,numdig)
    print(sortedList)

if __name__ == '__main__':
    main()