"""
**Circular Array:**

Implement a CircularArray class that supports an array-like data structure which can be efficiently rotated. If possible,
the class should use a generic type (also called a template), and should support iteration via the standard for
(Obj o : circularArray) notation.
"""
from typing import List, TypeVar, Union

T = TypeVar("T", int, bool)


class CircularArray(List[T]):
    def __init__(self, size: int):  # noqa
        self.size = size
        self.arr = [None for _ in range(size)]
        self.pointer = 0

    def __setitem__(self, key: int, value: T):
        key = self.convert(key)
        self.arr[key] = value

    def __getitem__(self, item: int) -> Union[T, None]:
        key = self.convert(item)
        return self.arr[key]

    def convert(self, key: int):
        return (self.pointer + key) % self.size

    def shift_right(self):
        self.pointer = (self.pointer + 1) % self.size

    def shift_left(self):
        self.pointer = (self.pointer - 1) % self.size

    def __iter__(self):
        return self

    def __next__(self):
        val = self.arr[self.pointer]
        pointer = (self.pointer + 1) % self.size
        self.pointer = pointer
        return val


circular_array = CircularArray[str](4)
circular_array[0] = 123
circular_array[1] = "hello"
