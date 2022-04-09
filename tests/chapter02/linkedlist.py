import random

from chapter02.linkedlist import LinkedList, Node


def test_node():
    simple_node = Node(random.randint(0, 10))


def test_linked_list():
    nodes = [Node(random.randint(0, 10)) for _ in range(10)]
    linkedlist = LinkedList(*nodes)
    for idx, node in enumerate(linkedlist):
        if idx < 9:
            assert node.right is not None
        else:
            assert node.right is None
