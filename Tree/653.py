# 653. Two Sum IV - Input is a BST

# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 9
# Output: true

# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 28
# Output: false

# Example 3:
# Input: root = [2, 1, 3], k = 4
# Output: true

# Example 4:
# Input: root = [2, 1, 3], k = 1
# Output: false

# Example 5:
# Input: root = [2, 1, 3], k = 3
# Output: true

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        dic = {}

        def dfs(root, k):
            if not root:
                return False
            if k - root.val in dic:
                return True
            dic[root.val] = 1

            return dfs(root.left, k) or dfs(root.right, k)

        return dfs(root, k)
