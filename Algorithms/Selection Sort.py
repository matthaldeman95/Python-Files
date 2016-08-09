import random

def findMinimum(list, startindex):
    """
    Finds minimum number in a list, starting from a given index
    :param list:  List to find minimum of
    :param startindex:  Index to start searching list from
    :return:
    """
    minVal = list[startindex]
    minIndex = startindex
    for n in range(startindex,len(list)):
        if list[n] < minVal:
            minVal = list[n]
            minIndex = n
    return (minVal,minIndex)

def SelectionSort(a):
    """
    Selection sort algorithm to sort list low to high
    :param a:  List to be sorted
    :return: Sorted list
    """
    for m in range(0,len(a)):
        minVal, minIndex = findMinimum(a,m)
        a[minIndex] = a[m]
        a[m] = minVal
    return a


if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,10)]
    print "Start list:  ", examplearray
    print "Sorted list:  ", SelectionSort(examplearray)


