#tri fusion bitonique non parallélisé

def bitonicSort_compare(array, i, j, increase):
    if (array[i] > array[j]) == increase:
        array.swap(i, j)

def bitonicSort_merge(array, beg, count, increase):
    if count == 1:
        return
    n = count//2
    for i in range(beg, beg+n):
        bitonicSort_compare(array, i, i+n, increase)
    bitonicSort_merge(array, beg, n, increase)
    bitonicSort_merge(array, beg+n, n, increase)

def rec_bitonicSort(array, beg, count, increase):
    if count == 1:
        return
    n = count//2
    rec_bitonicSort(array, beg, n, True)
    rec_bitonicSort(array, beg+n, n, False)
    bitonicSort_merge(array, beg, count, increase)

def bitonicSort(array, ascending=True):
    power = 1
    while power < array.size:
        power *= 2
    assert(array.size == power)
    rec_bitonicSort(array, 0, power, ascending)