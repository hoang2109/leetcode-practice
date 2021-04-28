# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]

# Example 2:
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]
# Explanation: [4, 9] is also accepted.


class Solution(object):
    def intersection(self, nums1, nums2):
        dic = {}

        for val in nums1:
            if not val in dic:
                dic[val] = 1

        rs = []
        for val in nums2:
            if val in dic:
                rs.append(val)
                del dic[val]

        return rs
