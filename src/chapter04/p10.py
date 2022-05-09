from chapter04.trees import BinaryNode, BinaryTree


def extend_node_with_null_values(node: BinaryNode):
    if node.left:
        extend_node_with_null_values(node.left)
    if node.right:
        extend_node_with_null_values(node.right)
    if not node.left:
        node.left = BinaryNode(None, node)
    if not node.right:
        node.right = BinaryNode(None, node)


def extend_tree_with_null_values(tree):
    root = tree.root
    extend_node_with_null_values(root)


def pre_order_traversal(node: BinaryNode, traversal_order: list = None):
    traversal_order = [] if traversal_order is None else traversal_order
    traversal_order.append(node.data)
    if node.left:
        pre_order_traversal(node.left, traversal_order)
    if node.right:
        pre_order_traversal(node.right, traversal_order)
    return traversal_order


def check_if_subtree(t1: BinaryTree, t2: BinaryTree) -> bool:
    extend_tree_with_null_values(t1)
    extend_tree_with_null_values(t2)
    t1_pre_order_traversal = pre_order_traversal(t1.root)
    t2_pre_order_traversal = pre_order_traversal(t2.root)
    return t2_pre_order_traversal in t1_pre_order_traversal
