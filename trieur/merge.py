#tri fusion

def mergeSort_merge(array, beg, end):
    n = end-beg
    resultat = n*[0]
    mid = beg + n//2
    it1 = beg
    it2 = mid
    it = 0

    while it != n:
        if it1 == mid:
            resultat[it] = array[it2]
            it2 += 1
        elif it2 == end:
            resultat[it] = array[it1]
            it1 += 1
        elif array[it1] > array[it2]:
            resultat[it] = array[it2]
            it2 += 1
        else:
            resultat[it] = array[it1]
            it1 += 1
        it += 1

    for it in range(0, n):
        array[beg + it] = resultat[it]

def rec_mergeSort(array, beg, end):
    n = end-beg
    if n == 1:
        return
    mid = beg + n//2
    rec_mergeSort(array, beg, mid)
    rec_mergeSort(array, mid, end)
    mergeSort_merge(array, beg, end)

def mergeSort(array):
    rec_mergeSort(array, 0, array.size)