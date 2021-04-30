# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0, 1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0, 1, 0]
# Output: 2
# Explanation: [0, 1](or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


class Solution(object):
    def findMaxLength(self, nums):
        dic = {}

        preSum = 0
        rs = 0

        for i, val in enumerate(nums):
            if val == 0:
                preSum += 1
            else:
                preSum -= 1

            if preSum == 0:
                rs = max(rs, i + 1)

            if preSum not in dic:
                dic[preSum] = i
            else:
                rs = max(rs, i - dic[preSum])

        return rs
