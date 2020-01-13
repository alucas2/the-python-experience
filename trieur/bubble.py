#tri à bulles

def bubbleSort(array):
    for i in range(array.size):
        for j in range(array.size-i-1):
            if array[j] > array[j+1]:
                array.swap(j, j+1)

def cocktailSort(array):
    beg = 0
    end = array.size-1
    while beg < end:
        nbeg = end
        nend = beg
        for j in range(beg, end):
            if array[j] > array[j+1]:
                array.swap(j, j+1)
                nend = j
        end = nend
        for j in range(end, beg-1, -1):
            if array[j] > array[j+1]:
                array.swap(j, j+1)
                nbeg = j+1
        beg = nbeg