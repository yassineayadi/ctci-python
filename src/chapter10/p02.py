from typing import Sequence


def merge(left: Sequence[str], right: Sequence[str]):
    len_left, len_right = len(left), len(right)
    merged = [None for _ in range(len_left + len_right)]
    i = j = k = 0
    while i < len_left and j < len_right:
        if ord(left[i]) < ord(right[j]):
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        merged[k] = left[i]
        k += 1
        i += 1
    while j < len_right:
        merged[k] = right[j]
        k += 1
        j += 1
    return merged

def merge_sort_string(array: Sequence[str]):
    if len(array) == 1:
        return array
    midpoint = len(array) // 2
    left = merge_sort_string(array[:midpoint])
    right = merge_sort_string(array[midpoint:])
    return merge(left, right)


def count_anagrams(text: str):
    words = text.split()
    sorted_words = [''.join(merge_sort_string(word)) for word in words]
    counts = dict()
    for word in sorted_words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts