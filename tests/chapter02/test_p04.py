import random

from chapter02.linkedlist import LinkedList, Node
from chapter02.p04 import partition_linkedlist


def test_partition_linkedlist():
    nodes = [Node(random.randint(0, 10)) for _ in range(0, 10)]
    linkedlist = LinkedList(*nodes)
    result = partition_linkedlist(linkedlist, 5)
    print(result)
