from dataclasses import dataclass, field
from typing import Any, List, Union


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
        if self.left is None:
            self.left = BinaryNode(data, parent=self)
            return self.left
        elif self.right is None:
            self.right = BinaryNode(data, parent=self)
            return self.right
        else:
            min_node = (
                self.left if self.left.height <= self.right.height else self.right
            )
            return min_node.insert(data)

    @property
    def height(self):
        right_height = self.right.height if self.right else 0
        left_height = self.left.height if self.left else 0
        return max([left_height, right_height]) + 1

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.data} (height={self.height})\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()

    def __repr__(self):
        return self.disp()


@dataclass
class BinarySearchNode(BinaryNode):

    parent: "BinarySearchNode" = field(default=None)
    left: "BinarySearchNode" = field(default=None)
    right: "BinarySearchNode" = field(default=None)

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinarySearchNode(data, parent=self)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinarySearchNode(data, parent=self)
        else:
            self.data = data

    def __repr__(self):
        return super().__repr__()


@dataclass
class BinaryTree:
    root: BinaryNode = field(default=None)

    def insert(self, data):
        if not self.root:
            self.root = BinaryNode(data)
            return self.root
        else:
            return self.root.insert(data)

    def __repr__(self):
        if self.root:
            return self.root.__repr__()
        else:
            return "Empty Tree"


@dataclass
class BinarySearchTree(BinaryTree):
    root: BinarySearchNode = field(default=None)

    def insert(self, data):
        if not self.root:
            self.root = BinarySearchNode(data)
        else:
            self.root.insert(data)

    def __repr__(self):
        return self.root.__repr__()


def in_order_traversal(node: BinarySearchNode):
    if node:
        in_order_traversal(node.left)
        print(node.data, " -> ", end="")
        in_order_traversal(node.right)


def pre_order_traversal(node: BinarySearchNode):
    if node:
        print(node.data, "->")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node: BinarySearchNode):
    if node:
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        print(node.data)
