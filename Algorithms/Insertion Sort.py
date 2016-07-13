import random


def insertionsort(a):

    A = []                                  #Empty list to store sort values
    A.append(a[0])                          #Append first value in a to A
    for n in range(1,len(a)):               #For all remaining values in a,
        m = n - 1
        key = A[m]                          #key to compare values of A to
        while m >= 0 and a[n] < key:        #only iterate if m has remaining values
                                            #and if the current a value is less than key
            if n == m+1:                    #Append to list if no A[m+1] value exists
                A.append(A[m])
            else:                           #else replace value
                A[m+1] = A[m]
            m -= 1                          #Continue moving left in A until index 0
            key = A[m]
        A[m+1] = a[n]                       #Once a[n] is no longer less than key, insert it here
    return A


if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,10)]
    print examplearray
    print insertionsort(examplearray)