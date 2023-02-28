# Used for array generation
from random import random

# Algorithm imports from local project
from algorithms.quicksort import quicksort
from algorithms.mergesort import mergesort
from algorithms.heapsort import heapsort
from algorithms.shellsort import shellsort

# Used for time measurement and graph plotting
import matplotlib.pyplot as plt
from time import perf_counter as time


def main():
    # Will generate 2n arrays of max 5 * 10^n random elements
    # Warning: any n > 5 will highly increase the time
    n = 5
    arr = [None] * (n * 2)

    # Will generate 2n arrays with random float numbers between 0 and 1
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = [random() for _ in range(10 ** ((i // 2) + 1))]
        else:
            arr[i] = [random() for _ in range(10 ** ((i // 2) + 1) * 5)]

    # Copy the generated arrays onto dedicated arrays
    quick_arr = arr.copy()
    merge_arr = arr.copy()
    heap_arr = arr.copy()
    shell_arr = arr.copy()

    # Time measurement for the quicksort algorithm
    quick_time = []
    print("Quicksort: ", end="")
    for i in range(len(quick_arr)):
        start = time()
        quick_arr[i] = quicksort(quick_arr[i])
        end = time()
        quick_time.append((end - start) * 1e3)
        print("#", end="")
    print("")

    # Time measurement for the mergesort algorithm
    merge_time = []
    print("Mergesort: ", end="")
    for i in range(len(merge_arr)):
        start = time()
        merge_arr[i] = mergesort(merge_arr[i])
        end = time()
        merge_time.append((end - start) * 1e3)
        print("#", end="")
    print("")

    # Time measurement for the heapsort algorithm
    heap_time = []
    print("Heapsort: ", end="")
    for i in range(len(heap_arr)):
        start = time()
        heap_arr[i] = heapsort(heap_arr[i])
        end = time()
        heap_time.append((end - start) * 1e3)
        print("#", end="")
    print()

    # Time measurement for the shellsort algorithm
    shell_time = []
    print("Shellsort: ", end="")
    for i in range(len(shell_arr)):
        start = time()
        shell_arr[i] = shellsort(shell_arr[i])
        end = time()
        shell_time.append((end - start) * 1e3)
        print("#", end="")
    print()

    # Store the no of elements for graph plotting
    elems = []
    for a in arr:
        elems.append(len(a))

    rate = []
    for i in range(2 * n):
        rate.append(i + 1)

    plt.plot(elems, quick_time, "-r")
    plt.title("Quicksort algorithm")
    plt.ylabel("Time (ms)")
    plt.xlabel("Number of elements")
    plt.show()

    plt.plot(elems, merge_time, "-g")
    plt.title("Mergesort algorithm")
    plt.ylabel("Time (ms)")
    plt.xlabel("Number of elements")
    plt.show()

    plt.plot(elems, heap_time,  "-b")
    plt.title("Heapsort algorithm")
    plt.ylabel("Time (ms)")
    plt.xlabel("Number of elements")
    plt.show()

    plt.plot(elems, shell_time, "-k")
    plt.title("Shellsort algorithm")
    plt.ylabel("Time (ms)")
    plt.xlabel("Number of elements")
    plt.show()

    plt.plot(rate, quick_time, "-r")
    plt.plot(rate, merge_time, "-g")
    plt.plot(rate, heap_time, "-b")
    plt.plot(rate, shell_time, "-k")
    plt.title("Rates of change over array length increase")
    plt.legend(["Quicksort", "Mergesort", "Heapsort", "Shellsort"])
    plt.ylabel("Time (ms)")
    plt.xlabel("Rate of change")
    plt.show()


if __name__ == '__main__':
    main()
