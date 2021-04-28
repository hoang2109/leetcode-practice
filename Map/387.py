# 387. First Unique Character in a String

# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1


class Solution(object):
    def firstUniqChar(self, s):
        dic = {}

        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i

        return -1
