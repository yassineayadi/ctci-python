from dataclasses import dataclass
from typing import Any


class EmptyStackError(Exception):
    pass


@dataclass
class StackNode:
    data: Any
    next: "StackNode"


class Stack:
    def __init__(self):
        self.top: StackNode = None  # noqa

    def push(self, data: Any):
        node = StackNode(data, next=self.top)
        self.top = node

    def pop(self) -> Any:
        if not self.top:
            raise EmptyStackError()
        current = self.top.data
        self.top = self.top.next
        return current

    def peek(self):
        if not self.top:
            raise EmptyStackError()
        return self.top.data

    def __iter__(self):
        while self.top:
            yield self.pop()

    def push_multiple(self, *data):
        for d in data:
            self.push(d)

    @classmethod
    def from_list(cls, data: list) -> "Stack":
        stack = cls()
        stack.push_multiple(*data)
        return stack


@dataclass
class QueueNode:
    data: Any
    next: "QueueNode"


class EmptyQueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data: Any):
        node = QueueNode(data, None)  # noqa
        if not self.first:
            self.first = self.last = node  # noqa
        else:
            self.last.next = node
            self.last = node

    def remove(self) -> Any:
        if not self.first:
            raise EmptyQueueError
        current = self.first
        self.first = self.first.next
        return current.data

    def peek(self):
        if not self.first:
            raise EmptyQueueError
        return self.first.data

    def pop(self):
        if not self.first:
            raise EmptyQueueError
        current = self.first
        self.first = current.next
        return current.data

    @property
    def is_empty(self) -> bool:
        return bool(self.first)

    def add_multiple(self, *data):
        for d in data:
            self.add(d)


class StackIsFullError(Exception):
    pass


class MultiStackFixedSize:
    def __init__(self, number_of_stacks, size_of_stack):
        self.array = [0] * number_of_stacks * size_of_stack
        self.current_size = [0] * number_of_stacks
        self.max_size = size_of_stack
        self.number_of_stacks = number_of_stacks

    def is_full(self, stack_number):
        if self.current_size[stack_number] >= self.max_size:
            raise StackIsFullError(f"Stack {stack_number} is currently full.")
        return False

    def add(self, stack_number, data):
        if not self.is_full(stack_number):
            idx = self.current_index(stack_number)
            self.array[idx] = data
            self.current_size[stack_number] += 1

    def current_index(self, stack_number) -> int:
        return self.max_size * stack_number + self.current_size[stack_number]
