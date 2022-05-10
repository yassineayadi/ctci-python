from chapter04.trees import BinaryNode, BinaryTree


def first_common_ancestor(left: BinaryNode, right: BinaryNode):
    # move to same level

    lowest_node = left if left.height <= right.height else right
    highest_node = left if left.height > right.height else right

    while lowest_node.height < highest_node.height:
        lowest_node = lowest_node.parent

    while lowest_node.parent != highest_node.parent:
        lowest_node = lowest_node.parent
        highest_node = highest_node.parent

    return lowest_node.parent
