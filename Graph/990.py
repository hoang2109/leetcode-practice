# 990. Satisfiability of Equality Equations

# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters(not necessarily different) that represent one-letter variable names.
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

# Example 1:
# Input: ["a==b", "b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

# Example 2:
# Input: ["b==a", "a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

# Example 3:
# Input: ["a==b", "b==c", "a==c"]
# Output: true

# Example 4:
# Input: ["a==b", "b!=c", "c==a"]
# Output: false

# Example 5:
# Input: ["c==c", "b==d", "x!=z"]
# Output: true

import collections


class Solution(object):
    def equationsPossible(self, equations):
        graph = collections.defaultdict(set)
        check = []

        for u, o, _, v in equations:
            if o == '=':
                graph[u].add(v)
                graph[v].add(u)
            else:
                check.append((u, v))

        def dfs(u, v, visited):
            if u == v:
                return True
            visited.add(u)

            for nei in graph[u]:
                if nei not in visited:
                    if dfs(nei, v, visited):
                        return True
            return False

        for u, v in check:
            visited = set()
            if dfs(u, v, visited):
                return False

        return True
