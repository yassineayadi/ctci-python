from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    value: Any
    left: "Node" = field(default=None)
    right: "Node" = field(default=None)

    def __repr__(self):
        return (
            f"Node(value={self.value}, left={self.left.value if self.left else None}, "
            f"right={self.right.value if self.right else None})"
        )


class LinkedList:
    def __init__(self, *nodes):
        for idx, node in enumerate(nodes):
            if idx == 0:
                self.current = node
            if idx != 0:
                node.left = nodes[idx - 1]
            if idx != len(nodes) - 1:
                node.right = nodes[idx + 1]

        self.direction = "right"

    def __repr__(self):
        return f"LinkedList at {self.current!r}"

    def __iter__(self):
        return self

    def iter_with_direction(self, direction: str = "right"):
        self.direction = direction
        return iter(self)

    def __next__(self):
        current = self.current
        if current is None:
            raise StopIteration
        self.current = getattr(self.current, self.direction)
        return current
