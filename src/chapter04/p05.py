from chapter04.trees import BinaryNode, BinaryTree


def validate_in_order_traversal(tree: BinaryNode):
    is_valid = True
    if tree.left:
        is_valid = is_valid and tree.left.data <= tree.data
        is_valid = is_valid and validate_in_order_traversal(tree.left)
    if tree.right:
        is_valid = is_valid and tree.data <= tree.right.data
        is_valid = is_valid and validate_in_order_traversal(tree.right)
    return is_valid


def validate_bst(tree: BinaryTree) -> bool:
    return validate_in_order_traversal(tree.root)
