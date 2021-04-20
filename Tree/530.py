# 530. Minimum Absolute Difference in BST

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:
# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return 0

        rs = float('inf')
        lastNode = None
        node = root
        stack = []

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if lastNode:
                    rs = min(rs, node.val - lastNode.val)
                lastNode = node
                node = node.right

        return rs
