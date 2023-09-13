def quicksort(arr: list) -> list:
    # Add a terminal condition
    if len(arr) < 2:
        return arr

    pivot = arr[-1]
    left = []
    middle = []
    right = []
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            middle.append(el)
    # By chunking the array into parts like this we can begin bitting pieces of it off
    # guaranteeing that it will eventaully shrink enough to reach the terminal condition.
    return quicksort(left) + middle + quicksort(right)


def inplace_quicksort(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(arr, lo, hi):
        pivot = arr[hi]
        i, j = lo - 1, lo

        while j < hi:
            if arr[j] < pivot:
                i += 1
                swap(arr, i, j)
            j += 1
        i += 1
        swap(arr, hi, i)
        return i

    def sort(arr, lo, hi):
        if hi <= lo:
            return

        pivot = partition(arr, lo, hi)
        sort(arr, lo, pivot - 1)
        sort(arr, pivot + 1, hi)

    sort(arr, 0, len(arr) - 1)
