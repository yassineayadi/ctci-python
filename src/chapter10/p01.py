"""
**Sorted Merge:**
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.
"""


def merge_two_sorted_arrays(larger: list[int], smaller: list[int]):
    size_larger, size_smaller = (
        len(larger),
        len(smaller),
    )
    actual_size_larger = sum([1 for _ in larger if _ is not None])
    i, j, k = actual_size_larger - 1, size_smaller - 1, size_larger - 1

    while j >= 0:
        if larger[i] > smaller[j]:
            larger[k] = larger[i]
            larger[i] = None
            i -= 1
        else:
            larger[k] = smaller[j]
            j -= 1
        k -= 1
    return larger
