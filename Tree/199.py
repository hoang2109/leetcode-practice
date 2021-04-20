# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1, 2, 3, null, 5, null, 4]
# Output: [1, 3, 4]

# Example 2:
# Input: root = [1, null, 3]
# Output: [1, 3]

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
    def rightSideView(self, root):
        if not root:
            return []

        rs = []
        queue = [root]

        while queue:
            tmp = None

            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            rs.append(tmp.val)
        return rs
