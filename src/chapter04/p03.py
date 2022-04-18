from typing import List

from chapter03.p05 import LinkedList
from chapter04.trees import BinarySearchNode


def dfs_recursive_binary_tree(
    tree: BinarySearchNode, levels: list = None, level: int = 0
) -> List[LinkedList]:
    levels = [LinkedList()] if levels is None else levels
    if (len(levels) - 1) < level:
        levels.append(LinkedList())

    levels[level].add(tree.data)
    if tree.left:
        dfs_recursive_binary_tree(tree=tree.left, level=level + 1, levels=levels)
    if tree.right:
        dfs_recursive_binary_tree(tree=tree.right, level=level + 1, levels=levels)

    return levels


def nodes_at_each_depth(root: BinarySearchNode):
    linkedlist_nodes = dfs_recursive_binary_tree(root)
    print(linkedlist_nodes)
