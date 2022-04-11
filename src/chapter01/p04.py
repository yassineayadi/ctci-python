# def is_palindrome_pythonic(left_word, right_word):
#     return sorted(left_word) == sorted(right_word)
#
#
# def is_palindrome_array(left_word, right_word):
#     if len(left_word) != len(right_word):
#         return False
#     for idx, val in enumerate(left_word):
#         if val != right_word[-idx]:
#             return False
#     return True
import string
from collections import Counter


def clean_phrase(phrase):
    return [c.lower() for c in phrase if c in string.ascii_letters]


def is_permutation_palindrome(phrase):
    counter = Counter(clean_phrase(phrase))
    return sum(v % 2 for v in counter.values()) <= 1


# def is_palindrome_array(word):
#
#     for val, rev in zip(word, reversed(word)):
#         if val != rev:
#             return False
#     return True

functions = [is_permutation_palindrome]
