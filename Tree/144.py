# 144. Binary Tree Preorder Traversal

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 2, 3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1, 2]
# Output: [1, 2]

# Example 5:
# Input: root = [1, null, 2]
# Output: [1, 2]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        rs = []
        node = root
        stack = []

        while node or stack:
            if node:
                rs.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        return rs
