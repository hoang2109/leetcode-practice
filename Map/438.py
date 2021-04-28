# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution(object):
    def findAnagrams(self, s, p):
        dic = {}

        for c in p:
            dic[c] = dic.get(c, 0) + 1

        rs = []
        matched = 0
        i = 0
        for j in range(len(s)):
            c = s[j]
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    matched += 1
            if matched == len(dic):
                rs.append(i)

            if j >= len(p) - 1:
                c = s[i]
                if c in dic:
                    if dic[c] == 0:
                        matched -= 1
                    dic[c] += 1
                i += 1

        return rs
