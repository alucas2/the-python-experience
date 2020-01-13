#tri par insertion

def insertionSort(array):
    for i in range(1, array.size):
        j = i
        while j >= 1 and array[j] < array[j-1]:
            array.swap(j, j-1)
            j -= 1
