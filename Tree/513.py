# 513. Find Bottom Left Tree Value

# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example 1:
# Input: root = [2,1,3]
# Output: 1

# Example 2:
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return None

        queue = [root]
        rs = None

        while queue:
            rs = queue[0]
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rs.val
