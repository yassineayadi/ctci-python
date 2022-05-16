"""
**Hash Table:***

Design and implement a hash table which uses chaining (linked lists) to handle collisions.
"""
from dataclasses import dataclass
from typing import Any, Generator


@dataclass
class Cell:
    data: Any
    next: "Cell" = None


@dataclass
class LinkedList:
    head: Cell | None = None
    tail: Cell | None = None
    size: int = 0

    def add(self, data):
        if self.head is None:
            self.head = self.tail = Cell(data)
        else:
            cell = Cell(data)
            self.tail.next = cell
            self.tail = cell
        self.size += 1

    def __iter__(self) -> Generator[Cell, None, None]:
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        return " -> ".join(cell.data for cell in self)

    def delete(self, data):
        temp, prev = self.head, None

        if temp.data == data:
            self.head = self.tail = temp.next
            return

        while temp:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
            del temp
        return


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.array = [LinkedList() for _ in range(size)]

    def __repr__(self):
        return "\n".join(f"[{idx}] {l}" for idx, l in enumerate(self.array))

    @property
    def needs_resize(self):
        pass

    def resize(self):
        pass

    @staticmethod
    def pre_hash(key):
        pre_hash = key.encode("utf-8")
        return int.from_bytes(pre_hash, "little")

    def hash(self, key):
        return key % self.size

    def get_key(self, key):
        return self.hash(self.pre_hash(key))

    def __setitem__(self, key, value):
        key = self.get_key(key)
        self.array[key].add(value)

    def __getitem__(self, item):
        for v in self.get_linked_list(item):
            if v.data == item:
                return v.data

    def get_linked_list(self, item) -> LinkedList:
        key = self.get_key(item)
        return self.array[key]

    def __delitem__(self, key):
        ll = self.get_linked_list(key)
        ll.delete(key)
