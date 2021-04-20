# 687. Longest Univalue Path

# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
# The length of the path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [5, 4, 5, 1, 1, 5]
# Output: 2

# Example 2:
# Input: root = [1, 4, 5, 4, 4, 5]
# Output: 2

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestUnivaluePath(self, root):
        self.rs = 0

        def dfs(root, prev):
            if not root:
                return 0

            left = dfs(root.left, root)
            right = dfs(root.right, root)

            self.rs = max(self.rs, left + right)

            if prev and root.val == prev.val:
                return max(left, right) + 1

            return 0

        dfs(root, None)

        return self.rs
