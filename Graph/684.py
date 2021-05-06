# 684. Redundant Connection

# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Example 1:
# Input: edges = [[1, 2], [1, 3], [2, 3]]
# Output: [2, 3]

# Example 2:
# Input: edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
# Output: [1, 4]

import collections


class Solution1(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(u, v, visited):
            if u == v:
                return True
            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    if dfs(nei, v, visited):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if dfs(u, v, visited):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

        return []


class Solution2(object):
    def findRedundantConnection(self, edges):
        parents = [-1] * len(edges)

        def find(x):
            if parents[x] == -1:
                return x
            return find(parents[x])

        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot != yRoot:
                parents[xRoot] = yRoot
                return False
            return True

        for u, v in edges:
            if union(u - 1, v - 1):
                return [u, v]

        return []
