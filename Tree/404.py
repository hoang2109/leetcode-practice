# 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:
# Input: root = [1]
# Output: 0

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        rs = 0
        if root.left and not root.left.left and not root.left.right:
            rs += root.left.val

        rs += self.sumOfLeftLeaves(root.left)
        rs += self.sumOfLeftLeaves(root.right)

        return rs
