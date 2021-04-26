# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i = 0
        rs = 0

        for j in range(len(s)):
            if s[j] in dic:
                dic[s[j]] += 1
            else:
                dic[s[j]] = 1

            while dic[s[j]] > 1:
                dic[s[i]] -= 1
                i += 1

            rs = max(rs, j - i + 1)

        return rs
