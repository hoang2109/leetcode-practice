# 114. Flatten Binary Tree to Linked List

# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Example 1:
# Input: root = [1, 2, 5, 3, 4, null, 6]
# Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    def flatten(self, root):
        self.prev = None

        def dfs(root):
            if not root:
                return
            if self.prev:
                self.prev.right = root
            self.prev = root

            left = root.left
            right = root.right

            root.left = None
            root.right = None

            dfs(left)
            dfs(right)

        dfs(root)


class Solution2(object):
    def flatten(self, root):
        if not root:
            return None

        prev = None
        stack = [root]

        while stack:
            node = stack.pop()

            if prev:
                prev.right = node
            prev = node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            node.right = None
            node.left = None
