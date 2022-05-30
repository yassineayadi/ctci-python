"""
Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The
array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
available, how would you print all duplicate elements in the array?
"""
from io import StringIO


def find_duplicates(stream: StringIO):
    bit_vector = 0
    while True:
        data = stream.readline()
        if data == "":
            break
        value = int(data.rstrip())
        vectorized = 1 << (value - 1)
        if vectorized & bit_vector != 0:
            print(vectorized)
        else:
            bit_vector |= vectorized
