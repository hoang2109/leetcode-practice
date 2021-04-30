# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2


class Solution(object):
    def subarraySum(self, nums, k):
        dic = {0: 1}
        currSum = 0
        rs = 0

        for val in nums:
            currSum += val

            if currSum - k in dic:
                rs += dic[currSum - k]

            if currSum in dic:
                dic[currSum] += 1
            else:
                dic[currSum] = 1

        return rs
