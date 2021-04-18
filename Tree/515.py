# 515. Find Largest Value in Each Tree Row

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1,null,2]
# Output: [1,2]

# Example 5:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -2^31 <= Node.val <= 2^31 - 1

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        if not root:
            return []

        queue = [root]
        rs = []

        while queue:
            maxRow = -float('inf')

            for _ in range(len(queue)):
                node = queue.pop(0)
                maxRow = max(maxRow, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(maxRow)

        return rs
