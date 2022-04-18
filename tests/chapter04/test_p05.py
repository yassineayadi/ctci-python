from chapter04.trees import BinarySearchTree, BinaryTree
from chapter04.p05 import validate_bst

bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

t = BinaryTree()
t.insert(5)
t.insert(4)
t.insert(6)
t.insert(3)
t.insert(6)
t.insert(5)
t.insert(2)


def test_validate_bst():
    assert validate_bst(bst) is True


def test_validate_standard_binary_tree():
    assert validate_bst(t) is False
