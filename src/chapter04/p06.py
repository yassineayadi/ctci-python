from chapter04.trees import BinarySearchNode


def next_node_from_child(tree: BinarySearchNode):
    while tree:
        if tree.left:
            tree = tree.left
        else:
            return tree


def next_node_from_parent(tree: BinarySearchNode):
    parent = tree.parent
    while parent.right == tree:
        parent = tree.parent
        if parent is None:
            return
    return parent


def next_node(tree: BinarySearchNode):
    if tree.right:
        return next_node_from_child(tree.right)
    return next_node_from_parent(tree)
