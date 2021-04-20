# 94. Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1, 2]
# Output: [2, 1]

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
    def inorderTraversal(self, root):
        rs = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            rs.append(root.val)
            dfs(root.right)

        dfs(root)

        return rs


class Solution2(object):
    def inorderTraversal(self, root):
        rs = []

        node = root
        stack = []

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                rs.append(node.val)
                node = node.right
        return rs
