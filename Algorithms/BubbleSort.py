import random

def bubbleSort(a):
    """
    Sorts a list of numbers low to high using bubble sort algorithm
    :param a:  Unsorted list
    :return:   Sorted list
    """
    swapped = True
    while swapped == True:
        swapped = False
        for index in range(0,len(a)-1):
            print a
            value = a[index]
            if value > a[index+1]:
                a[index] = a[index+1]
                a[index+1] = value
                swapped = True
    return a




if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,10)]
    print "Example list", examplearray
    print bubbleSort(examplearray)