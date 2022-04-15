from chapter04.trees_and_graphs import (
    Tree,
    BinaryTree,
    in_order_traversal,
    pre_order_traversal,
    post_order_traversal,
)
from chapter04.heaps import MaxHeap, MinHeap


def test_create_tree():
    tree = Tree()
    tree.add_to_last(1)
    tree.add_to_last(2)


def test_create_binary_tree():
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    in_order_traversal(tree.root)


def test_maxheap():
    maxheap = MaxHeap(20)
    maxheap.insert(1)
    maxheap.insert(2)
    maxheap.insert(3)
    maxheap.insert(4)
    maxheap.insert(5)
    maxheap.insert(6)
    maxheap.insert(7)
    maxheap.insert(8)
    assert maxheap.get_right_child(0) == 6
    assert maxheap.get_left_child(0) == 7


def test_maxheap_max_heapify():
    maxheap = MaxHeap(20)
    maxheap.insert(1)
    maxheap.insert(2)
    maxheap.insert(3)
    maxheap.insert(9)
    maxheap.insert(10)
    maxheap.insert(3)
    maxheap.insert(1)
    maxheap.insert(1)
    for node_idx in range(1, maxheap.current_size):
        assert maxheap.get(node_idx) <= maxheap.get_parent(node_idx)


def test_maxheap_get_max():
    maxheap = MaxHeap(20)
    maxheap.insert(1)
    maxheap.insert(40)
    maxheap.insert(3)
    maxheap.insert(2)
    maxheap.insert(10)
    assert maxheap.get_max() == 40


def test_minheap_remove_last():
    minheap = MinHeap(20)
    minheap.insert(1)
    minheap.insert(2)
    minheap.insert(3)
    minheap.insert(9)
    minheap.insert(10)
    minheap.insert(3)
    minheap.insert(1)
    minheap.insert(1)
    assert minheap.last_idx == 7
    minheap.remove_last()
    assert minheap.last_idx == 6


def test_minheap_heapify_down():
    minheap = MinHeap(20)
    minheap.insert(1)
    minheap.insert(2)
    minheap.insert(9)
    minheap.insert(10)
    minheap.insert(3)
    minheap.insert(4)
    minheap.insert(5)
    # minheap.heapify_down(node_idx=0)


def test_remove_min_min_heap():
    minheap = MinHeap(20)
    minheap.insert(1)
    minheap.insert(2)
    minheap.insert(9)
    minheap.insert(10)
    minheap.insert(3)
    minheap.insert(4)
    minheap.insert(5)
    minheap.remove_min()
    print(minheap)


def test_remove_max_maxheap():
    maxheap = MaxHeap(20)
    maxheap.insert(1)
    maxheap.insert(2)
    maxheap.insert(3)
    maxheap.insert(4)
    maxheap.insert(5)
    maxheap.insert(6)
    maxheap.insert(7)
    maxheap.insert(8)
    maxheap.remove_max()
    print(maxheap)
