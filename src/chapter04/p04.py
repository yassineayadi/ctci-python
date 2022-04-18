from chapter04.trees import BinarySearchNode


def is_balanced(tree: BinarySearchNode):
    if tree.left and tree.right:
        balanced = abs(tree.left.height - tree.right.height) <= 1
        balanced = balanced and is_balanced(tree.left)
        balanced = balanced and is_balanced(tree.right)

        return balanced
    return True