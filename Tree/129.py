# 129. Sum Root to Leaf Numbers

# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.

# A leaf node is a node with no children.

# Example 1:
# Input: root = [1, 2, 3]
# Output: 25
# Explanation:
# The root-to-leaf path 1 -> 2 represents the number 12.
# The root-to-leaf path 1 -> 3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:
# Input: root = [4, 9, 0, 5, 1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4 -> 9 -> 5 represents the number 495.
# The root-to-leaf path 4 -> 9 -> 1 represents the number 491.
# The root-to-leaf path 4 -> 0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        rs = []

        def dfs(root, preSum):
            if not root:
                return
            preSum = preSum * 10 + root.val

            if not root.left and not root.right:
                rs.append(preSum)

            dfs(root.left, preSum)
            dfs(root.right, preSum)

        dfs(root, 0)

        return sum(rs)
