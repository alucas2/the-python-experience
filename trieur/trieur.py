import pygame as pyg
from pygame import midi
pyg.init()
pyg.midi.init()
from Array import Array
from shuffle import shuffle, isSorted
from bubble import bubbleSort, cocktailSort
from insertion import insertionSort
from quick import quickSort
from merge import mergeSort
from radix import radixLSDSort, countingSort
from heap import heapSort
from bitonic import bitonicSort

a = Array(range(0, 512))

a.drawRate = 7
shuffle(a)

a.drawRate = 15
#bubbleSort(a)
#insertionSort(a)
#cocktailSort(a)
#mergeSort(a)
#quickSort(a)
#radixLSDSort(a)
#countingSort(a)
#heapSort(a)
bitonicSort(a)

a.drawRate = 7
assert(isSorted(a))

pyg.time.wait(200)
pyg.midi.quit()
pyg.quit()