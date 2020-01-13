import random

def isSorted(array, ascending=True):
    for i in range(array.size-1):
        if (array[i+1] < array[i]) == ascending:
            return False
    return True

def shuffle(array):
    for i in range(array.size-1, 0, -1):
        r = random.randint(0,i)
        array.swap(i, r)
