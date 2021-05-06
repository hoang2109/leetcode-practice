# 547. Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# Output: 3


import collections


class Solution1(object):
    def findCircleNum(self, isConnected):
        graph = collections.defaultdict(set)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)

        visited = set()

        def dfs(i):
            visited.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)

        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1

        return count


class Solution2(object):
    def findCircleNum(self, isConnected):
        parents = [-1] * len(isConnected)

        def find(x):
            if parents[x] == -1:
                return x
            return find(parents[x])

        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot != yRoot:
                parents[xRoot] = yRoot

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i, j)
        count = 0
        for p in parents:
            if p == -1:
                count += 1

        return count
