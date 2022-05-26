"""
**Recursive Multiply:**
Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
"""


def recursive_multiply(left: int, right: int):
    smaller = left if left <= right else right
    bigger = left if left > right else right

    if smaller == 1:
        return bigger
    if bigger == 1:
        return smaller
    if smaller == 0 or bigger == 0:
        return 0

    result, multiplier = bigger, smaller

    while multiplier > 1:
        result <<= 1
        multiplier >>= 1
    if smaller % 2 == 0:
        return result
    return result + bigger
