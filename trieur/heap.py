#tri par tas

def heap_parent(i): return (i-1)//2
def heap_left(i): return 2*i + 1
def heap_right(i): return 2*i + 2

def siftDown(array, beg, end):
    root = beg
    
    while heap_left(root) <= end:
        left = heap_left(root)
        right = left + 1
        swap = root

        if array[swap] < array[left]:
            swap = left
        if right <= end and array[swap] < array[right]:
            swap = right
        
        if swap == root:
            break
        else:
            array.swap(swap, root)
            root = swap

def heapify(array):
    for i in range(heap_parent(array.size-1), -1, -1):
        siftDown(array, i, array.size-1)

def heapSort(array):
    heapify(array)
    for i in range(array.size-1, 0, -1):
        array.swap(0, i)
        siftDown(array, 0, i-1)
