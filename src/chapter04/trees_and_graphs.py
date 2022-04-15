from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class TreeNode:

    data: Any
    children: List["TreeNode"] = field(default_factory=list)
    parent: "TreeNode" = field(default=None)


class Tree:
    root: TreeNode
    last: TreeNode

    def __init__(self):
        self.root = self.last = None  # noqa

    def add_to_last(self, data):
        if self.root is None:
            self.root = self.last = TreeNode(data=data)
        elif self.last == self.root:
            last_parent = self.root
            node = TreeNode(data, parent=last_parent)
            last_parent.children.append(node)
        else:
            last_parent = self.last.parent
            node = TreeNode(data=data, parent=last_parent)
            self.last.parent.children.append(node)


@dataclass
class BinaryNode:

    data: Any
    parent: "BinaryNode" = field(default=None)
    left: "BinaryNode" = field(default=None)
    right: "BinaryNode" = field(default=None)

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinaryNode(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinaryNode(data)
        else:
            self.data = data


@dataclass
class BinaryTree:
    root: BinaryNode = field(default=None)

    def insert(self, data):
        if not self.root:
            self.root = BinaryNode(data)
        else:
            self.root.insert(data)


def in_order_traversal(node: BinaryNode):
    if node:
        in_order_traversal(node.left)
        print(node.data, " -> ", end="")
        in_order_traversal(node.right)


def pre_order_traversal(node: BinaryNode):
    if node:
        print(node.data, "->")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node: BinaryNode):
    if node:
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        print(node.data)
