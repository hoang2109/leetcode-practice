# 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference(possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.
# Follow up: Can you solve it with time complexity O(height of tree)?

# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
# Output: [5, 4, 6, 2, null, null, 7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5, 4, 6, 2, null, null, 7], shown in the above BST.
# Please notice that another valid answer is [5, 2, 6, null, 4, null, 7] and it's also accepted.

# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, 7], key = 0
# Output: [5, 3, 6, 2, 4, null, 7]
# Explanation: The tree does not contain a node with value = 0.

# Example 3:
# Input: root = [], key = 0
# Output: []

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                tmp = root.right
                root.right = None
                return tmp
            if not root.right:
                tmp = root.left
                root.left = None
                return tmp
            tmp = self.findMin(root.right)
            root.val = tmp.val
            root.right = self.deleteNode(root.right, tmp.val)
        return root

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root
