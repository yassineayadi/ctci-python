from chapter04.trees import BinarySearchNode
from chapter04.p04 import is_balanced


def _gen_balanced_2():
    root = BinarySearchNode(7)
    root.left = BinarySearchNode(2)
    root.left.left = BinarySearchNode(4)
    root.right = BinarySearchNode(3)
    root.right.left = BinarySearchNode(8)
    root.right.right = BinarySearchNode(9)
    root.right.right.right = BinarySearchNode(10)
    return root


def _gen_unbalanced_1():
    root = BinarySearchNode(1)
    root.left = BinarySearchNode(2)
    root.left.left = BinarySearchNode(4)
    root.left.right = BinarySearchNode(5)
    root.left.right.right = BinarySearchNode(6)
    root.left.right.right.right = BinarySearchNode(7)
    root.right = BinarySearchNode(3)
    root.right.left = BinarySearchNode(8)
    root.right.right = BinarySearchNode(9)
    root.right.right.right = BinarySearchNode(10)
    root.right.right.right.right = BinarySearchNode(11)
    return root


def _gen_unbalanced_2():
    tree = BinarySearchNode(1)
    tree.left = BinarySearchNode(2)
    tree.right = BinarySearchNode(9)
    tree.right.left = BinarySearchNode(10)
    tree.left.left = BinarySearchNode(3)
    tree.left.right = BinarySearchNode(7)
    tree.left.right.right = BinarySearchNode(5)
    tree.left.left.left = BinarySearchNode(6)
    tree.left.right.left = BinarySearchNode(12)
    tree.left.right.left.left = BinarySearchNode(16)
    tree.left.right.left.right = BinarySearchNode(0)
    return tree


def test_is_balanced():
    balanced = _gen_balanced_2()
    assert is_balanced(balanced) is True


def test_is_unbalanced():
    unbalanced_1 = _gen_unbalanced_1()
    assert is_balanced(unbalanced_1) is False
    unbalanced_2 = _gen_unbalanced_2()
    assert is_balanced(unbalanced_2) is False
