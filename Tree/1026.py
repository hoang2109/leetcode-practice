# 1026. Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val | and A is an ancestor of B.
# A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

# Example 1:
# Input: root = [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]

# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below:
# |8 - 3 | = 5
# |3 - 7 | = 4
# |8 - 1 | = 7
# |10 - 13 | = 3
# Among all possible differences, the maximum value of 7 is obtained by | 8 - 1 | = 7.

# Example 2:
# Input: root = [1, null, 2, null, 0, 3]
# Output: 3

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        self.rs = 0

        def dfs(root, maxx, minn):
            if not root:
                self.rs = max(self.rs, maxx - minn)
                return
            maxx = max(maxx, root.val)
            minn = min(minn, root.val)

            dfs(root.left, maxx, minn)
            dfs(root.right, maxx, minn)

        dfs(root, -float('inf'), float('inf'))

        return self.rs
