# 222. Count Complete Tree Nodes

# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6]
# Output: 6

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [1]
# Output: 1

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)

        if leftHeight != rightHeight:
            left = self.countNodes(root.left)
            right = self.countNodes(root.right)

            return left + right + 1

        return 2 ** leftHeight - 1

    def getLeftHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count

    def getRightHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count
