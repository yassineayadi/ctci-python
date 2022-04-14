from typing import Any

from chapter03.stack_and_queue import Stack


class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.tempstack = Stack()

    def push(self, data):
        while self.peek() is not None and data > self.peek():
            self.tempstack.push(self.pop())
        while not self.tempstack.is_empty:
            self.push(self.tempstack.pop())


