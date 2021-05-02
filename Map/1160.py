# 1160. Find Words That Can Be Formed by Characters

# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars(each character can only be used once).
# Return the sum of lengths of all good strings in words.


# Example 1:
# Input: words = ["cat", "bt", "hat", "tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:
# Input: words = ["hello", "world", "leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation:
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

import collections


class Solution(object):
    def countCharacters(self, words, chars):
        counter = collections.Counter(chars)
        rs = 0

        for word in words:
            wordDic = {}

            for ch in word:
                wordDic[ch] = wordDic.get(ch, 0) + 1

            found = True
            for ch in wordDic:
                if ch in counter and counter[ch] >= wordDic[ch]:
                    continue
                else:
                    found = False
                    break

            if found:
                rs += len(word)

        return rs
