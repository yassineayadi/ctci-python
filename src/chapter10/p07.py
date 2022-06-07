"""
Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to
generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
this task.
"""
from typing import Generator
import csv


class Reader:
    def __init__(self, file: str):
        self.file = file
        self.io = open(file, "r")
        self.reader = csv.reader(self.io)

    def read_chunk(self):
        data = next(self.read())
        return data

    def read(self) -> Generator[list[str], None, None]:
        for data in self.reader:
            yield data


def find_missing_int(file: str):
    """
    Reads through file chunk-wise and appends to bit-vector. Returns first integer not matching bit-vector.
    """
    reader = Reader(file)
    bit_vector = 0
    for data in reader.read():
        for integer in data:
            bits = 1 << int(integer) - 1
            bit_vector |= bits
    for i in range(1, 2 ** 32):
        bits = 1 << int(i) - 1
        if bits & bit_vector == 0:
            return i
