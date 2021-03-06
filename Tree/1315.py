# 1315. Sum of Nodes with Even-Valued Grandparent

# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
# If there are no nodes with an even-valued grandparent, return 0.

# Example 1:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumEvenGrandparent(self, root):
        if not root:
            return 0

        def dfs(root, parent, grandParent):
            if not root:
                return 0
            rs = 0
            if grandParent and grandParent.val % 2 == 0:
                rs += root.val
            grandParent = parent
            parent = root

            rs += dfs(root.left, parent, grandParent)
            rs += dfs(root.right, parent, grandParent)
            return rs

        return dfs(root, None, None)
