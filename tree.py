import sys
from collections import deque

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create a new stack"""
        self.__s = []

    def peek(self):
        """Get the value of the top item in the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.__s[-1]

    def push(self, item):
        """Add an item to the stack"""
        self.__s.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.__s.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.__s

class Queue:
    """Queue implementation as a deque"""

    def __init__(self):
        """Create a new queue"""
        self.__q = deque()

    def peek(self):
        """Get the value of the front item in the queue"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.__q[0]

    def enqueue(self, item):
        """Add an item to the queue"""
        self.__q.append(item)

    def dequeue(self):
        """Remove an item from the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.__q.popleft()

    def is_empty(self):
        """Check if the queue is empty"""
        return not self.__q

class Node:
    """Node class for representing a node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node."""
        if value is None or isinstance(value, int):
            self.__data = value
        else:
            raise ValueError("data must be an int or None.")

    @property
    def left(self):
        """Get the left child of the node."""
        return self.__left

    @left.setter
    def left(self, node):
        """Set the left child of the node."""
        if node is None or isinstance(node, Node):
            self.__left = node
        else:
            raise ValueError("left must be a Node or None.")

    @property
    def right(self):
        """Get the right child of the node."""
        return self.__right

    @right.setter
    def right(self, node):
        """Set the right child of the node."""
        if node is None or isinstance(node, Node):
            self.__right = node
        else:
            raise ValueError("right must be a Node or None.")


class Tree:
    """Tree class for representing a binary search tree."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert data into the binary search tree."""

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = self.root

            while current is not None:
                parent = current

                if data < current.data:
                    current = current.left
                else:
                    current = current.right

            if data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    # Return True if both trees are similar. False otherwise.
    # tree is also a Tree type
    def is_similar(self, tree):
        return self._is_similar_helper(self.root, tree.root)

    def _is_similar_helper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        else:
            return (node1.data == node2.data and 
                    self._is_similar_helper(node1.left, node2.left) and 
                    self._is_similar_helper(node1.right, node2.right))

    # Return a list of nodes at a given level from left to right.
    def get_level(self, level):
        nodes_at_level = []
        self._get_level_helper(self.root, level, nodes_at_level)
        return nodes_at_level

    def _get_level_helper(self, node, level, nodes_at_level):
        if node is None:
            return
        if level == 0:
            nodes_at_level.append(node.data)
        else:
            self._get_level_helper(node.left, level - 1, nodes_at_level)
            self._get_level_helper(node.right, level - 1, nodes_at_level)

    # Return the height of the tree
    def get_height(self):
        return self._get_height_helper(self.root)

    def _get_height_helper(self, node):
        if node is None:
            return -1
        else:
            left_height = self._get_height_helper(node.left)
            right_height = self._get_height_helper(node.right)
            return 1 + max(left_height, right_height)

    # Return the number of nodes in the tree.
    def num_nodes(self):
        return self._num_nodes_helper(self.root)

    def _num_nodes_helper(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._num_nodes_helper(node.left) + self._num_nodes_helper(node.right)

    # Returns the range of values stored in the tree.
    def range(self):
        if self.root is None:
            return 0
        min_value, max_value = self._range_helper(self.root)
        print("min_value:", min_value)
        print("max_value:", max_value)
        return max_value - min_value if min_value is not None and max_value is not None else 0

    def _range_helper(self, node):
        if node is None:
            return float('inf'), -float('inf')
        else:
            left_min, left_max = self._range_helper(node.left)
            right_min, right_max = self._range_helper(node.right)
            min_value = min(node.data, left_min, right_min)
            max_value = max(node.data, left_max, right_max)
            return min_value, max_value

    # Returns the list of the node that you see from left side.
    # The order of the output should be from top to down.
    def left_side_view(self):
        left_view = []
        self._left_side_view_helper(self.root, 0, left_view)
        return left_view

    def _left_side_view_helper(self, node, depth, left_view):
        if node is None:
            return
        if depth == len(left_view):
            left_view.append(node.data)
        self._left_side_view_helper(node.left, depth + 1, left_view)
        self._left_side_view_helper(node.right, depth + 1, left_view)

    # Returns the sum of the value of all leaves.
    def sum_leaf_nodes(self):
        return self._sum_leaf_nodes_helper(self.root)

    def _sum_leaf_nodes_helper(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.data
        left_sum = self._sum_leaf_nodes_helper(node.left)
        right_sum = self._sum_leaf_nodes_helper(node.right)
        return left_sum + right_sum

def main():
    """Main function. Feel free to write your own code here to test."""

if __name__ == "__main__":
    main()
