from random import random

from algorithms.quicksort import quicksort
from algorithms.mergesort import mergesort
from algorithms.heapsort import heapsort


def main():
    arr = [[random() for _ in range(10 ** i)] for i in range(1, 6)]

    quick_arr = arr.copy()
    merge_arr = arr.copy()
    heap_arr = arr.copy()

    for a in quick_arr:
        a = quicksort(a)

    for a in merge_arr:
        a = mergesort(a)

    for a in heap_arr:
        a = heapsort(a)


if __name__ == '__main__':
    main()
