import random

def linearSearch(a,value):
    """

    :param a:  Array to be searched
    :param value:  Value to search for in list
    :return: index n of a such that a[n] == value, or NIL if not found
    """
    for n in range(0,len(a)):
        if a[n] == value:
            return n
    return "NIL"

if __name__ == '__main__':
    random.seed(0)
    examplearray = [random.randint(0,20) for k in range(0,50)]
    print "List: ", examplearray
    value = int(input('Value to find:  '))
    print linearSearch(examplearray,value)

