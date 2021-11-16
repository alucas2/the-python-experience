import pygame as pyg
from pygame import midi
pyg.init()
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

while True:
    i = input("Command: ")
    if i == "exit":                 break
    elif i == "shuffle":            shuffle(a)
    elif i == "bubble":             bubbleSort(a)
    elif i == "insertion":          insertionSort(a)
    elif i == "cocktail":           cocktailSort(a)
    elif i == "merge":              mergeSort(a)
    elif i == "quick":              quickSort(a)
    elif i == "radix":              radixLSDSort(a)
    elif i == "counting":           countingSort(a)
    elif i == "heap":               heapSort(a)
    elif i == "bitonic":            bitonicSort(a)
    elif i == "issorted":           isSorted(a)

pyg.quit()