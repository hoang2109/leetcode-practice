# 501. Find Mode in Binary Search Tree

# Given the root of a binary search tree(BST) with duplicates, return all the mode(s)(i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:
# Input: root = [1, null, 2, 2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMode(self, root):
        self.maxFreq = 0
        dic = {}

        def dfs(root):
            if not root:
                return
            if root.val not in dic:
                dic[root.val] = 0
            dic[root.val] += 1
            self.maxFreq = max(self.maxFreq, dic[root.val])

            dfs(root.left)
            dfs(root.right)

        rs = []
        dfs(root)

        for key, val in dic.items():
            if val == self.maxFreq:
                rs.append(key)

        return rs
