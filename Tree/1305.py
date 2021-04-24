# 1305. All Elements in Two Binary Search Trees

# Given two binary search trees root1 and root2.
# Return a list containing all the integers from both trees sorted in ascending order.

# Example 1:
# Input: root1 = [2, 1, 4], root2 = [1, 0, 3]
# Output: [0, 1, 1, 2, 3, 4]

# Example 2:
# Input: root1 = [0, -10, 10], root2 = [5, 1, 7, 0, 2]
# Output: [-10, 0, 0, 1, 2, 5, 7, 10]

# Example 3:
# Input: root1 = [], root2 = [5, 1, 7, 0, 2]
# Output: [0, 1, 2, 5, 7]

# Example 4:
# Input: root1 = [0, -10, 10], root2 = []
# Output: [-10, 0, 10]

# Example 5:
# Input: root1 = [1, null, 8], root2 = [8, 1]
# Output: [1, 1, 8, 8]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getAllElements(self, root1, root2):

        rs = []
        stack1, stack2 = [], []

        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                node = stack1.pop()
                rs.append(node.val)
                root1 = node.right
            elif not stack1 or (stack2 and stack2[-1].val <= stack1[-1].val):
                node = stack2.pop()
                rs.append(node.val)
                root2 = node.right

        return rs
