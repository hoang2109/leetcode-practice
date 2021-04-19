# 897. Increasing Order Search Tree

# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Example 2:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def increasingBST(self, root):
        self.curr = TreeNode()
        newRoot = self.curr

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.curr.right = TreeNode(root.val)
            self.curr = self.curr.right
            dfs(root.right)

        dfs(root)

        return newRoot.right


class Solution2(object):
    def increasingBST(self, root):
        if not root:
            return None

        newRoot = TreeNode()
        curr = newRoot

        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                curr.right = TreeNode(node.val)
                curr = curr.right
                node = node.right

        return newRoot.right
