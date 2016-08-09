import random
from InsertionSort import insertionsort

def mergeSort(a):
    """

    :param a:
    :return:
    """
    print "Splitting", a
    if len(a)>1:
        midpt = len(a)/2
        left = a[:midpt]
        right = a[midpt:]

        mergeSort(left)
        mergeSort(right)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    print "Merging", a



if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,6)]
    mergeSort(examplearray)



