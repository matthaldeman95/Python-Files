import random

def quicksort(array):
    """

    :param array:
    :return:
    """
    leftarray = []
    rightarray = []
    equalarray = []
    if len(array) > 1:
        pivotvalue = array[len(array)-1]
        for val in array:
            if val < pivotvalue:
                leftarray.append(val)
            if val == pivotvalue:
                equalarray.append(val)
            if val > pivotvalue:
                rightarray.append(val)
        print array, leftarray, equalarray, rightarray
        return quicksort(leftarray) + equalarray + quicksort(rightarray)

    else:
        return array




if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,10)]
    print "Starting list:", examplearray
    print quicksort(examplearray)
