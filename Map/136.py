# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Example 1:
# Input: nums = [2, 2, 1]
# Output: 1

# Example 2:
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


class Solution(object):
    def singleNumber(self, nums):
        dic = {}

        for _, val in enumerate(nums):
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
        for k, v in dic.items():
            if v == 1:
                return k

        return -1
