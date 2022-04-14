from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Any, Union

from chapter03.p03 import QueueFromStacks


class AnimalType(Enum):
    DOG = "dog"
    CAT = "cat"


@dataclass
class Animal:

    name: str
    type: AnimalType


@dataclass
class Node:
    data: Any
    next: Union["Node", None]


@dataclass
class LinkedList:
    head: "Node" = field(default=None)
    tail: "Node" = field(default=None)
    current: "Node" = field(default=None)

    def add(self, data):
        if not self.head:
            self.head = self.tail = self.current = Node(data, None)
        else:
            tail = Node(data, None)
            self.tail.next = tail
            self.tail = tail

    def pop_head(self):
        head = self.head
        if self.current == self.head:
            self.current = self.head.next
        self.head = self.head.next
        return head.data

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def pop_any(self, node):
        prev_node = None

        for n in self:
            if n.next == node:
                prev_node = n

        prev_node.next = node.next
        return node.data


class AnimalShelterQueue(LinkedList):
    def enqueue(self, animal: Animal):
        self.add(animal)

    def dequeue_any(self):
        return self.pop_head()

    def dequeue_cat(self):
        for animal in self:
            if animal.data.type == AnimalType.CAT:
                return self.pop_any(animal)

    def dequeue_dog(self):
        for animal in self:
            if animal.data.type == AnimalType.DOG:
                return self.pop_any(animal)
