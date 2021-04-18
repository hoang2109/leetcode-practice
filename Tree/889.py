# 889. Construct Binary Tree from Preorder and Postorder Traversal

# Return any binary tree that matches the given preorder and postorder traversals.
# Values in the traversals pre and post are distinct positive integers.

# Example 1:
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

# Note:
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructFromPrePost(self, pre, post):
        dic = {}
        for i, v in enumerate(post):
            dic[v] = i
        self.preIndex = 0

        def build(left, right):
            if left > right:
                return None
            node = TreeNode(pre[self.preIndex])
            self.preIndex += 1

            if left == right:
                return node
            postIndex = dic[pre[self.preIndex]]

            node.left = build(left, postIndex)
            node.right = build(postIndex + 1, right - 1)
            return node
        return build(0, len(post) - 1)
