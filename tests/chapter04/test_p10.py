from chapter04.trees import BinaryTree
from chapter04.p10 import extend_tree_with_null_values, pre_order_traversal



def test_extend_tree_with_null_values():
    t = BinaryTree()
    t.insert(5)
    t.insert(4)
    t.insert(6)
    t.insert(3)
    extend_tree_with_null_values(t)

def test_pre_order_traversal():
    t = BinaryTree()
    t.insert(5)
    t.insert(4)
    t.insert(6)
    t.insert(3)
    traversal_order = pre_order_traversal(t.root)
    print(traversal_order)
    print(t.root)
    assert traversal_order is not None