# 1002. Find Common Characters

# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list(including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
# You may return the answer in any order.

# Example 1:
# Input: ["bella", "label", "roller"]
# Output: ["e", "l", "l"]

# Example 2:
# Input: ["cool", "lock", "cook"]
# Output: ["c", "o"]


class Solution(object):
    def commonChars(self, A):
        dic = dict()

        for ch in A[0]:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        for k in dic:
            for word in A[1:]:
                cnt = word.count(k)
                if cnt < dic[k]:
                    dic[k] = cnt

        rs = []

        for ch in dic:
            if dic[ch] > 0:
                rs += [ch] * dic[ch]

        return rs
