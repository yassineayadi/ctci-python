from chapter04.trees import (
    BinarySearchTree,
    Tree,
    in_order_traversal,
)
from chapter04.graphs import bfs_non_recursive, dfs_non_recursive, dfs_recursive


def test_create_tree():
    tree = Tree()
    tree.add_to_last(1)
    tree.add_to_last(2)


def test_create_binary_tree():
    tree = BinarySearchTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    in_order_traversal(tree.root)


def test_depth_first_search_recursive(graph):
    assert dfs_recursive(graph, starting_node="1") == [
        "1",
        "2",
        "6",
        "7",
        "8",
        "9",
        "4",
        "5",
        "3",
    ]


def test_depth_first_search_non_recursive(graph):
    assert dfs_non_recursive(graph, starting_node="1") == [
        "1",
        "3",
        "2",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]


def test_breadth_first_search(graph):
    assert bfs_non_recursive(graph, starting_node="1") == [
        "1",
        "2",
        "3",
        "6",
        "4",
        "7",
        "5",
        "8",
        "9",
    ]


