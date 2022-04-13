import pytest

from src.chapter03.stack_and_queue import (
    Stack,
    Queue,
    MultiStackFixedSize,
    StackIsFullError,
)


def test_create_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3


def test_loop_over_stack():
    data = [1, 2, 3]
    stack = Stack.from_list(data)
    for x, y in zip(stack, reversed(data)):
        assert x == y


def test_create_queue():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert queue.peek() == 1
    assert queue.remove() == 1




