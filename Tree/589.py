# 589. N-ary Tree Preorder Traversal

# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value(See examples)


# Example 1:
# Input: root = [1, null, 3, 2, 4, null, 5, 6]
# Output: [1, 3, 5, 6, 2, 4]

# Example 2:
# Input: root = [1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8,
#                null, 9, 10, null, null, 11, null, 12, null, 13, null, null, 14]
# Output: [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]


# Constraints:
# The number of nodes in the tree is in the range[0, 104].
# 0 <= Node.val <= 10 ^ 4
# The height of the n-ary tree is less than or equal to 1000.


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        rs = []

        def dfs(root):
            if not root:
                return
            rs.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return rs


class Solution2(object):
    def preorder(self, root):
        if not root:
            return []

        rs = []
        stack = [root]

        while stack:
            node = stack.pop()
            rs.append(node.val)

            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])

        return rs
