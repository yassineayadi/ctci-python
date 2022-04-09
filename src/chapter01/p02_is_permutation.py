from collections import Counter


def is_permutation_pythonic(left: str, right: str):
    left_counter, right_counter = Counter(left), Counter(right)
    return left_counter == right_counter


def is_permutation_index(left: str, right: str):
    left_counter = [0] * 128
    right_counter = [0] * 128
    for v in left:
        left_counter[ord(v)] += 1

    for v in right:
        right_counter[ord(v)] += 1

    for left_count, right_count in zip(left_counter, right_counter):
        if left_count != right_count:
            return False
    return True


functions = [is_permutation_pythonic, is_permutation_index]
