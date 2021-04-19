# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 2

# Example 2:
# Input: root = [2, null, 3, null, 4, null, 5, null, 6]
# Output: 5

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        queue = [root]
        rs = 0

        while queue:
            rs += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return rs

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rs
