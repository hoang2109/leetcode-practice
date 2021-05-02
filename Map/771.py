# 771. Jewels and Stones

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0


class Solution1(object):
    def numJewelsInStones(self, jewels, stones):
        dic = {}

        for s in stones:
            dic[s] = dic.get(s, 0) + 1

        rs = 0
        for j in jewels:
            if j in dic:
                rs += dic[j]

        return rs


class Solution2(object):
    def numJewelsInStones(self, jewels, stones):
        rs = 0
        for c in stones:
            if c in jewels:
                rs += 1
        return rs
