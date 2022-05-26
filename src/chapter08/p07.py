"""
**Permutations without Dups:**

Write a method to compute all permutations of a string of unique characters.
"""


def make_unique_set(arr: str) -> list:
    return list(set(arr))


def insert_char_at(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end


def compute_all_permutations_of_a_string(arr: str):
    permutations = []
    if arr is None:
        return None
    if len(arr) == 0:
        permutations.append(" ")
        return permutations
    unique_set = make_unique_set(arr)
    first = unique_set[0]
    remainder = unique_set[1:]
    words = compute_all_permutations_of_a_string(remainder)
    for word in words:
        index = 0
        for _ in word:
            s = insert_char_at(word, first, index)
            permutations.append(s)
            index += 1
    return permutations
