# 18. 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets[nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Example 2:
# Input: nums = [2, 2, 2, 2, 2], target = 8
# Output: [[2, 2, 2, 2]]


class Solution1(object):
    def fourSum(self, nums, target):
        def twoSum(nums, target):
            dic = {}
            rs = []
            for i in range(len(nums)):
                if len(rs) == 0 or rs[-1][1] != nums[i]:
                    if target - nums[i] in dic:
                        rs.append([target - nums[i], nums[i]])
                dic[nums[i]] = i
            return rs

        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            rs = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, arr in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        rs.append([nums[i]] + arr)
            return rs

        nums.sort()
        return kSum(nums, target, 4)


class Solution2(object):
    def fourSum(self, nums, target):
        nums.sort()
        rs = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        rs.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return rs
