def is_unique_pythonic(strng: str):
    if len(strng) > 128:
        return False
    return len(set(strng)) == len(strng)


def is_unique_index(strng: str):
    arr = [False] * 128
    for v in strng:
        val = ord(v)
        if arr[val] is True:
            return False
        arr[val] = True
    return True


def is_unique_bitshift(strng: str):
    checker = 0
    for v in strng:
        if (checker & (1 << ord(v))) > 0:
            return False
        checker |= 1 << ord(v)
    return True


functions = [is_unique_bitshift, is_unique_index, is_unique_pythonic]
