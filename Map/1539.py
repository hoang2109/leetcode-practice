# 1539. Kth Missing Positive Number

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.

# Example 1:
# Input: arr = [2, 3, 4, 7, 11], k = 5
# Output: 9
# Explanation: The missing positive integers are[1, 5, 6, 8, 9, 10, 12, 13, ...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1, 2, 3, 4], k = 2
# Output: 6
# Explanation: The missing positive integers are[5, 6, 7, ...]. The 2nd missing positive integer is 6.

import collections


class Solution1(object):
    def findKthPositive(self, arr, k):
        num = k
        i = 0
        while i < len(arr) and arr[i] <= num:
            num += 1
            i += 1
        return num


class Solution2(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        if n == 0:
            return 1

        missing = []
        nums = collections.Counter(arr)

        for i in range(1, max(nums) + k + 1):
            if not nums[i]:
                missing.append(i)

        return missing[k-1]


class Solution3(object):
    def findKthPositive(self, arr, k):
        l, r = 0, len(arr) - 1
        while l <= r:
            p = l + (r - l) // 2
            if arr[p] - p - 1 < k:
                l = p + 1
            else:
                r = p - 1

        return l + k
