# 637. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: root = [3,9,20,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return 0

        rs = []

        queue = [root]
        while queue:
            summ = 0.0
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                summ += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(summ / size)

        return rs
