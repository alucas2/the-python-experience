#tri par base

def maxValue(array):
    resultat = 0
    for i in range(array.size):
        v = array[i].getValue()
        if v > resultat:
            resultat = v
    return resultat


def radix_countingSort(array, base, power):
    resultat = array.size * [0]
    offsets = base * [0]
    
    for i in range(array.size):
        d = array[i].getValue()//power % base
        offsets[d] += 1
    for d in range(1, base):
        offsets[d] += offsets[d-1]

    #parcours en sens inverse pour un tri stable
    for i in range(array.size-1, -1, -1):
        d = array[i].getValue()//power % base
        offsets[d] -= 1
        pos = offsets[d]
        resultat[pos] = array[i]

    for i in range(array.size):
        array[i] = resultat[i]


def radixLSDSort(array, base=2):
    m = maxValue(array)
    power = 1
    while m // power > 0:
        radix_countingSort(array, base, power)
        power *= base

def countingSort(array):
    m = maxValue(array)
    radix_countingSort(array, m+1, 1)