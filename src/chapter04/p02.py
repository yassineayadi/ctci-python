from chapter04.trees import BinarySearchTree, BinarySearchNode


def create_binary_tree_with_minimal_height(data: list):
    mid_idx = len(data) // 2
    midpoint = data[mid_idx]
    root = BinarySearchNode(midpoint)
    if len(data) > 1:
        left_data = data[0:mid_idx]
        right_data = data[mid_idx + 1 :]
        root.left = create_binary_tree_with_minimal_height(left_data)
        root.right = create_binary_tree_with_minimal_height(right_data)
    return root
