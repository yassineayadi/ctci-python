from chapter04.trees import BinarySearchNode
from chapter04.p03 import nodes_at_each_depth

node_h = BinarySearchNode("H")
node_g = BinarySearchNode("G")
node_f = BinarySearchNode("F")
node_e = BinarySearchNode("E", left=node_g)
node_d = BinarySearchNode("D", left=node_h)
node_c = BinarySearchNode("C", left=node_f)
node_b = BinarySearchNode("B", left=node_d, right=node_e)
node_a = BinarySearchNode("A", left=node_b, right=node_c)


def test_nodes_at_each_depth():
    tree = node_a
    nodes_at_each_depth(tree)
