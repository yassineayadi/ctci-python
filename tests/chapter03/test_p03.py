from chapter03.p03 import QueueFromStacks


def test_queue_from_two_stacks():
    data = [1, 2, 3, 4, 5]
    queue = QueueFromStacks()
    queue.add_multiple(*data)
    assert queue.peek() == 1
