import random
from InsertionSort import insertionsort

def binarySearch(list, value):
    lowindex = 0
    highindex = len(list)-1
    while lowindex <= highindex:
        midpt = lowindex + (highindex-lowindex)/2
        if list[midpt] == value:
            return midpt
        elif value < list[midpt]:
            highindex = midpt - 1
        else:
            lowindex = midpt + 1
    return "Not found"



if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,10)]
    examplearray = insertionsort(examplearray,0)
    print "Example list:  ", examplearray
    number = input('Number to search for:  ')
    print binarySearch(examplearray, number)
