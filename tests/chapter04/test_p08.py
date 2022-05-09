from chapter04.p08 import first_common_ancestor
from chapter04.trees import BinaryTree



def test_first_common_ancestor():
    t = BinaryTree()
    t.insert(5)
    t.insert(4)
    t.insert(6)
    t.insert(3)
    left = t.insert(6)
    right = t.insert(2)
    ancestor = first_common_ancestor(left, right)
    assert ancestor == t.root
