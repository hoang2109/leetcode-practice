# 1302. Deepest Leaves Sum

# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:
# Input: root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
# Output: 15

# Example 2:
# Input: root = [6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]
# Output: 19

# Constraints:
# The number of nodes in the tree is in the range[1, 104].
# 1 <= Node.val <= 100

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        if not root:
            return 0

        queue = [root]
        rs = 0

        while queue:
            tmp = 0

            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rs = tmp

        return rs


class Solution2(object):
    def deepestLeavesSum(self, root):
        sums = []

        def dfs(root, lv):
            if not root:
                return
            if lv == len(sums):
                sums.append(root.val)
            else:
                sums[lv] += root.val

            dfs(root.left, lv + 1)
            dfs(root.right, lv + 1)

        dfs(root, 0)

        return sums[-1]
