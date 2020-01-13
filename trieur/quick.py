import random

#tri rapide

def partition1(array, beg, end):
    pivot = array[end]
    frontiere = beg

    for i in range(beg, end):
        if array[i] < pivot:
            array.swap(i, frontiere)
            frontiere += 1

    array.swap(frontiere, end)
    return frontiere

def partition2(array, beg, end):
    pivot = array[random.randint(beg, end)]
    it1 = beg
    it2 = end

    while it1 < it2:
        while array[it1] < pivot:
            it1 += 1
        while array[it2] > pivot:
            it2 -= 1
        array.swap(it1, it2)

    return it1

partitionFunc = partition2

def rec_quickSort(array, beg, end):
    if beg >= end:
        return
    frontiere = partitionFunc(array, beg, end)
    rec_quickSort(array, beg, frontiere-1)
    rec_quickSort(array, frontiere+1, end)

def quickSort(array):
    rec_quickSort(array, 0, array.size-1)
