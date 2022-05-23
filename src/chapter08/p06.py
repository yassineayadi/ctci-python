"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one).You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks
"""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: "Node" = None


@dataclass
class Stack:
    first: Node = None

    def push(self, value: int):
        if self.first is None:
            self.first = Node(value)
        else:
            self.first = Node(value, self.first)

    @property
    def peek(self):
        return self.first.value

    def pop(self):
        value = self.first.value
        self.first = self.first.next
        return value

    def __iter__(self):
        current = self.first
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        return " -> ".join(str(value) for value in self)


class MultiStack:
    def __init__(self, number_of_stacks: int):
        self.stacks = [Stack() for _ in range(number_of_stacks)]

    def get_stack(self, idx: int):
        return self.stacks[idx]

    def push_stack(self, idx: int, value: int):
        stack = self.stacks[idx]
        stack.push(value)

    def pop_stack(self, idx: int):
        stack = self.stacks[idx]
        stack.pop()

    def __iter__(self):
        for stack in self.stacks:
            yield stack

    def __repr__(self):
        return "\n" + "".join(
            f"[{idx}]: {repr(stack)}\n" for idx, stack in enumerate(self)
        )


class TowerOfHanoi:
    def __init__(self, size: int = 10):
        self.size = size
        self.multi_stack = MultiStack(3)
        self._init_first_stack(size)

    def _init_first_stack(self, size: int):
        for i in reversed(range(size)):
            self.multi_stack.get_stack(0).push(i)

    def move_from_to(self, disk: int, source: int, target: int, auxiliary: int):
        if disk > 0:
            self.move_from_to(disk - 1, source, auxiliary, target)
            self.multi_stack.get_stack(target).push(
                self.multi_stack.get_stack(source).pop()
            )
            self.move_from_to(disk - 1, auxiliary, target, source)

    def solve(self, source: int, target: int, auxiliary: int):
        self.move_from_to(self.size, source, target, auxiliary)
