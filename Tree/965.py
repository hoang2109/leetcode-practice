# 965. Univalued Binary Tree

# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Example 1:
# Input: [1, 1, 1, 1, 1, null, 1]
# Output: true

# Example 2:
# Input: [2, 2, 2, 5, 2]
# Output: false

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isUnivalTree(self, root):
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
