from dataclasses import dataclass, field
from typing import Any, Sequence
from copy import deepcopy


@dataclass
class Node:
    value: Any = field(default=None)
    prev: "Node" = field(default=None)
    next: "Node" = field(default=None)

    def __repr__(self):
        return (
            f"Node(value={self.value}, left={self.prev.value if self.prev else None}, "
            f"right={self.next.value if self.next else None})"
        )

    def __lt__(self, other: "Node"):
        return self.value < other.value

    def __eq__(self, other: "Node"):
        return self.value == other.value

    def __gt__(self, other: "Node"):
        return self.value > other.value

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)

    def delete(self):
        if self.next and self.prev:
            self.next.prev = self.prev
            self.prev.next = self.next
        elif self.next:
            self.next.prev = None
        elif self.prev:
            self.prev.next = None


class LinkedList:
    def __init__(self, *nodes):
        if nodes:
            self.head = nodes[0]
            self.current = nodes[0]
            for idx, node in enumerate(nodes):
                if idx != 0:
                    node.prev = nodes[idx - 1]
                if idx != len(nodes) - 1:
                    node.next = nodes[idx + 1]
                else:
                    self.tail = node
        else:
            self.current = Node()
            self.head = self.tail = None
        self.direction = "right"

    def __repr__(self):
        nodes = " -> ".join([str(node.value) for node in self])
        return f"LinkedList {nodes}"

    def __iter__(self):
        current = self.current
        while current:
            yield current
            current = current.next

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = self.current = node
        else:
            self.tail.next = node
            self.tail = node
        if not self.head.next:
            self.head.next = node
            self.tail.prev = node
            node.prev = self.head

    def add_after(self, node, after_node):
        after_node = deepcopy(after_node)
        for n in self:
            if n == node:
                if n.next:
                    n.next.prev = after_node
                    after_node.next = n.next
                else:
                    after_node.next = None
                n.next = after_node
                after_node.prev = n
                break

    def add_before(self, node, before_node):
        before_node = deepcopy(before_node)
        for n in self:
            if n == node:
                if n.prev:
                    n.prev.next = before_node
                    before_node.prev = n.prev
                else:
                    before_node.prev = None
                    self.head = self.current = before_node
                n.prev = before_node
                before_node.next = n
                # self.current = before_node
                break

    def iter_with_direction(self, direction: str = "right"):
        self.direction = direction
        return iter(self)

    def delete_current(self):
        current = self.current
        if self.current.prev:
            self.current = self.current.prev
        elif self.current.next:
            self.current = self.current.next
        current.delete()

    @classmethod
    def from_list(cls, arr: Sequence) -> "LinkedList":

        nodes = [Node(value=item) for item in arr]
        return cls(*nodes)

    @classmethod
    def from_integers(cls, integers: int) -> "LinkedList":
        integers = [int(i) for i in str(integers)]
        integers.reverse()
        return cls.from_list(integers)

    def to_list(self) -> list:
        return [node.value for node in self if node.value]
