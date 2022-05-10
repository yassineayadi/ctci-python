from dataclasses import dataclass, field
from random import choices

from chapter04.p10 import pre_order_traversal
from chapter04.trees import BinaryNode, BinaryTree
from random import choice


@dataclass
class AugmentedBinaryNodeWithSize(BinaryNode):
    left: "AugmentedBinaryNodeWithSize" = field(default=None)
    right: "AugmentedBinaryNodeWithSize" = field(default=None)

    def insert(self, data):
        if not self.left:
            self.left = AugmentedBinaryNodeWithSize(data, self)
        elif not self.right:
            self.right = AugmentedBinaryNodeWithSize(data, self)
        elif self.left.height < self.right.height:
            self.left.insert(data)
        else:
            self.right.insert(data)

    @property
    def left_size(self):
        if self.left:
            return self.left.size
        return 0

    @property
    def right_size(self):
        if self.right:
            return self.right.size
        return 0

    @property
    def size(self):
        return self.left_size + self.right_size + 1


class AugmentedBinaryTreeWithSize(BinaryTree):
    root: "AugmentedBinaryNodeWithSize" = field(default=None)


def random_node_slow_solution(tree: BinaryTree):
    array = pre_order_traversal(tree.root)
    return choice(array)


def traverse_probabilistically(current: AugmentedBinaryNodeWithSize):
    current, current_chance = current, 1
    left, left_chance = (current.left, current.left_size) if current.left else (None, 0)
    right, right_chance = (
        (current.right, current.right_size) if current.right else (None, 0)
    )
    [node] = choices(
        [current, left, right], [current_chance, left_chance, right_chance]
    )
    if node == left:
        traverse_probabilistically(node)
    elif node == right:
        traverse_probabilistically(node)
    else:
        return node


def random_choice_fast_solution(tree):
    return traverse_probabilistically(tree.root)
