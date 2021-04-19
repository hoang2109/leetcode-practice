# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself(i.e., symmetric around its center).

# Example 1:
# Input: root = [1, 2, 2, 3, 4, 4, 3]
# Output: true

# Example 2:
# Input: root = [1, 2, 2, null, 3, null, 3]
# Output: false

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):

        def isMirror(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            if root1.val != root2.val:
                return False

            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

        if not root:
            return True

        return isMirror(root.left, root.right)
