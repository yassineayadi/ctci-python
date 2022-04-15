import sys
from abc import ABC, abstractmethod
from operator import ge as greater_or_equal, le as less_or_equal
from typing import Callable


class Heap(ABC):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.current_size = 0
        self.heap = [0] * (maxsize + 1)
        self.heap[0] = -1 * sys.maxsize

    def __repr__(self):
        return self.heap[:self.current_size].__repr__()

    def insert(self, data):
        self.heap[self.current_size] = data
        self.current_size += 1
        self.heapify(self.last_idx)

    def heapify(self, node_idx):
        self._heapify(node_idx)

    @abstractmethod
    def _heapify(self, node_idx):
        raise NotImplementedError()

    def get_parent(self, node_idx):
        if node_idx > 0:
            parent_idx = self.get_parent_idx(node_idx)
            return self.heap[parent_idx]

    def get_parent_idx(self, node_idx):  # noqa
        if node_idx > 0:
            return (node_idx - 1) // 2

    def get_left_child(self, node_idx):
        left_idx = (node_idx * 2) + 1
        return self.heap[left_idx]

    def has_left_child(self, node_idx) -> bool:
        return bool(self.get_left_child(node_idx))

    def has_right_child(self, node_idx) -> bool:
        return bool(self.get_right_child(node_idx))

    def get_left_child_idx(self, node_idx):  # noqa
        return (node_idx * 2) + 1

    def get_right_child(self, node_idx):
        right_idx = (node_idx * 2) + 2
        return self.heap[right_idx]

    def get_right_child_idx(self, node_idx):  # noqa
        return (node_idx * 2) + 2

    def swap(self, left_idx, right_idx):
        self.heap[left_idx], self.heap[right_idx] = (
            self.heap[right_idx],
            self.heap[left_idx],
        )

    def get(self, node_idx):
        return self.heap[node_idx]

    @property
    def last(self):
        return self.heap[self.current_size - 1]

    @property
    def last_idx(self):
        return self.current_size - 1

    @property
    def first_idx(self):
        return 0

    def remove_last(self):
        last = self.last
        self.heap[self.last_idx] = 0
        self.current_size -= 1
        return last

    def heapify_down(self, node_idx, comp: Callable[..., bool]):
        if any([self.has_left_child(node_idx), self.has_right_child(node_idx)]):
            left_idx = self.get_left_child_idx(node_idx)
            right_idx = self.get_right_child_idx(node_idx)

            right_child = self.get_right_child(node_idx)
            left_child = self.get_left_child(node_idx)
            current = self.get(node_idx)

            min_idx = left_idx if comp(left_child, right_child) else right_idx
            min_child = left_child if comp(left_child, right_child) else right_idx
            if comp(min_child, current):
                self.swap(node_idx, min_idx)
                self.heapify_down(min_idx, comp)


class MaxHeap(Heap):
    def get_max(self):
        return self.heap[0]

    def _heapify(self, node_idx):
        if node_idx > 0:
            parent_idx = self.get_parent_idx(node_idx)
            if self.get(node_idx) > self.get(parent_idx):
                self.swap(node_idx, parent_idx)
                self.max_heapify(parent_idx)

    def max_heapify(self, node_idx):
        self.heapify(node_idx)

    def remove_max(self):
        self.swap(self.first_idx, self.last_idx)
        self.heapify_down(self.first_idx, greater_or_equal)
        self.remove_last()


class MinHeap(Heap):
    def get_min(self):
        return self.heap[0]

    def _heapify(self, node_idx):
        if node_idx > 0:
            parent_idx = self.get_parent_idx(node_idx)
            if self.get(node_idx) < self.get(parent_idx):
                self.swap(node_idx, parent_idx)
                self.min_heapify(parent_idx)

    def min_heapify(self, node_idx):
        return self.heapify(node_idx)

    def remove_min(self):
        self.swap(self.first_idx, self.last_idx)
        self.heapify_down(self.first_idx, less_or_equal)
        self.remove_last()