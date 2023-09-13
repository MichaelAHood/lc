from sorting.quicksort import quicksort, inplace_quicksort

import random


def test_quicksort() -> None:
    for _ in range(10):
        unsorted = [random.randint(1, 1000) for _ in range(100)]
        assert quicksort(unsorted) == sorted(unsorted)


def test_inplace_quicksort() -> None:
    for _ in range(10):
        unsorted = [random.randint(1, 1000) for _ in range(100)]
        inplace_quicksort(unsorted)
        assert unsorted == sorted(unsorted)
