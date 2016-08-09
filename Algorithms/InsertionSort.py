import random


def insertionsort(a, dir):
    """
    Performs insertion sort on a list of integers
    :param a: list to be sorted
    :param dir: 0 (forward, low to high), 1 (backward, high to low)
    :return: sorted list
    """

    A = []
    A.append(a[0])
    for n in range(1, len(a)):
        m = n - 1
        key = A[m]
        while m >= 0 and (a[n] < key if dir == 0 else a[n] > key):
            if n == m + 1:
                A.append(A[m])
            else:
                A[m + 1] = A[m]
            m -= 1
            key = A[m]
        if n == m + 1:
            A.append(a[n])
        else:
            A[m + 1] = a[n]
    return A





if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,10000)]

    print "Starting list: ", examplearray
    print "Forward: ", insertionsort(examplearray,0)
    print "Backward: ", insertionsort(examplearray,1)