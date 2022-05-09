import pytest

from chapter04.trees import BinaryTree


@pytest.fixture
def graph():
    return {
        "1": ["2", "3"],
        "2": ["1", "6", "4"],
        "3": ["1"],
        "4": ["2", "5"],
        "5": ["4"],
        "6": ["7"],
        "7": ["8"],
        "8": ["9"],
        "9": [],
    }


@pytest.fixture
def adjacency_list():
    return [
        [2],  # 0
        [2, 3],  # 1
        [1, 6, 4, 0],  # 2
        [1],  # 3
        [2, 5],  # 4
        [4],  # 5
        [7],  # 6
        [8],  # 7
        [9],  # 8
        [],  # 9
    ]


@pytest.fixture
def btree():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(-3)
    tree.insert(3)

    tree.root.left.insert(1)
    tree.root.left.right.insert(2)
    tree.root.right.insert(11)
    tree.root.left.left.insert(3)
    tree.root.left.left.insert(-2)
    tree.root.left.right.insert(1)
    return tree
