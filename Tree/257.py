# 257. Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Example 1:
# Input: root = [1, 2, 3, null, 5]
# Output: ["1->2->5", "1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(root, tmp, rs):
            if not root:
                return
            tmp += str(root.val)
            if not root.left and not root.right:
                rs.append(tmp)
            tmp += '->'
            dfs(root.left, tmp, rs)
            dfs(root.right, tmp, rs)

        rs = []
        dfs(root, '', rs)

        return rs
