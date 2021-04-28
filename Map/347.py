# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        dic = collections.Counter(nums)

        heap = []

        for i in dic:
            heap.append((-dic[i], i))

        heapq.heapify(heap)

        rs = []
        for _ in range(k):
            rs.append(heapq.heappop(heap)[1])

        return rs
