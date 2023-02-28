# Shellsort algorithm implementation
def shellsort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if array[i + gap] > array[i]:

                    break
                else:
                    array[i + gap], array[i] = array[i], array[i + gap]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2
    return array
