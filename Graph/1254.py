# 1254. Number of Closed Islands

# Given a 2D grid consists of 0s(land) and 1s(water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally(all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

# Example 1:
# Input: grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
#     1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water(group of 1s).

# Example 2:
# Input: grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
# Output: 1

# Example 3:
# Input: grid = [[1, 1, 1, 1, 1, 1, 1],
#                [1, 0, 0, 0, 0, 0, 1],
#                [1, 0, 1, 1, 1, 0, 1],
#                [1, 0, 1, 0, 1, 0, 1],
#                [1, 0, 1, 1, 1, 0, 1],
#                [1, 0, 0, 0, 0, 0, 1],
#                [1, 1, 1, 1, 1, 1, 1]]
# Output: 2


class Solution(object):
    def closedIsland(self, grid):
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 0:
                return
            grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        if len(grid) < 3:
            return 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m - 1] == 0:
                dfs(i, m - 1)

        for i in range(m):
            if grid[0][i] == 0:
                dfs(0, i)
            if grid[n - 1][i] == 0:
                dfs(n - 1, i)

        rs = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    rs += 1

        return rs
