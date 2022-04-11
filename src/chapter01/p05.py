# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) aw
from collections import Counter


# def one_insert_away(left_word: str, right_word: str):
#     insert_count = 0
#     max_length = max(len(left_word), len(right_word))


def one_insert_away(shorter, longer):
    edited = False
    i, j = 0, 0
    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def one_edit_away(left_word, right_word):
    edit_count = 0
    for left, right in zip(left_word, right_word):
        if left != right:
            edit_count += 1
    return edit_count <= 1


def is_one_away(left_word, right_word):
    if len(left_word) == len(right_word):
        return one_edit_away(left_word, right_word)
    elif len(left_word) - 1 == len(right_word):
        return one_insert_away(right_word, left_word)
    elif len(left_word) + 1 == len(right_word):
        return one_insert_away(left_word, right_word)
    else:
        return False


# def is_one_away(left_word, right_word):
#     left_counter = Counter(left_word)
#     right_counter = Counter(right_word)
#     intersect = left_counter - right_counter
#     delta = sum([abs(v) for v in intersect.values()])
#     return delta <= 1 and len(set(left_word).symmetric_difference(set(right_word))) <= 2
#     # for v in intersect.values():
#     #     if abs(v) > 1:
#     #         return False


functions = [is_one_away]
