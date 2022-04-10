from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    value: Any = field(default=None)
    left: "Node" = field(default=None)
    right: "Node" = field(default=None)

    def __repr__(self):
        return (
            f"Node(value={self.value}, left={self.left.value if self.left else None}, "
            f"right={self.right.value if self.right else None})"
        )

    def delete(self):
        if self.right and self.left:
            self.right.left = self.left
            self.left.right = self.right
        elif self.right:
            self.right.left = None
        elif self.left:
            self.left.right = None


class LinkedList:
    def __init__(self, *nodes):
        if nodes:
            self.head = nodes[0]
            self.current = nodes[0]
            for idx, node in enumerate(nodes):
                if idx != 0:
                    node.left = nodes[idx - 1]
                if idx != len(nodes) - 1:
                    node.right = nodes[idx + 1]
                else:
                    self.tail = node
        else:
            self.current = Node()
        self.direction = "right"

    def __repr__(self):
        return f"LinkedList {[' <-> '.join(node.value for node in self)]}"
        # return f"LinkedList at {self.current!r}"

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        if current is None:
            raise StopIteration
        self.current = getattr(self.current, self.direction)
        return current

    def iter_with_direction(self, direction: str = "right"):
        self.direction = direction
        return iter(self)

    def delete_current(self):
        current = self.current
        if self.current.left:
            self.current = self.current.left
        elif self.current.right:
            self.current = self.current.right
        current.delete()

    @classmethod
    def from_list(cls, arr: list) -> "LinkedList":
        nodes = [Node(value=item) for item in arr]
        return cls(*nodes)

    def to_list(self) -> list:
        return [node.value for node in self if node.value]
