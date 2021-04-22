# 113. Path Sum II

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: []

# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(root, targetSum, tmp, rs):
            if not root:
                return
            tmp.append(root.val)

            if not root.left and not root.right and root.val == targetSum:
                rs.append(list(tmp))
            dfs(root.left, targetSum - root.val, tmp, rs)
            dfs(root.right, targetSum - root.val, tmp, rs)
            tmp.pop()

        rs = []
        dfs(root, targetSum, [], rs)

        return rs
