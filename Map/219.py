# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1, 2, 3, 1], k = 3
# Output: true

# Example 2:
# Input: nums = [1, 0, 1, 1], k = 1
# Output: true

# Example 3:
# Input: nums = [1, 2, 3, 1, 2, 3], k = 2
# Output: false


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}

        for i, val in enumerate(nums):
            if val in dic and abs(i - dic[val]) <= k:
                return True
            dic[val] = i

        return False
