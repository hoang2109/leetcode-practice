# 107. Binary Tree Level Order Traversal II

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[15, 7], [9, 20], [3]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        rs = []
        queue = [root]

        while queue:
            sz = len(queue)
            tmp = []
            for _ in range(sz):
                node = queue.pop(0)
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs.append(tmp)

        return reversed(rs)
