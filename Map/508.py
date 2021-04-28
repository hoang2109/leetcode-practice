# 508. Most Frequent Subtree Sum

# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.
# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node(including the node itself).

# Example 1:
# Input: root = [5, 2, -3]
# Output: [2, -3, 4]

# Example 2:
# Input: root = [5, 2, -5]
# Output: [2]

# Definition for a binary tree node.

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findFrequentTreeSum(self, root):
        memo = collections.defaultdict(int)
        self.dfs(root, memo)
        if not memo:
            return []

        max_freq = max(memo.values())
        res = []
        for k, v in memo.items():
            if v == max_freq:
                res.append(k)

        return res

    def dfs(self, node, memo):
        # 1. termination:
        if not node:
            return 0

        # recursion on left
        left = self.dfs(node.left, memo)
        # recursion on right
        right = self.dfs(node.right, memo)
        # consider current node val
        cur = node.val

        # total sum at current node.
        cur_sum = cur + left + right
        memo[cur_sum] += 1

        return cur_sum
