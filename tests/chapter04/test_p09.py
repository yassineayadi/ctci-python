from chapter04.p09 import get_sequence
from chapter04.trees import BinarySearchTree

t = BinarySearchTree()

t.insert(3)
t.insert(2)
t.insert(4)
t.insert(1)
# t.insert(4)
# t.insert(5)


def test_find_bst_sequence():
    sequence = get_sequence(t.root)
    print(sequence)