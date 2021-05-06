# 1020. Number of Enclaves

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent(4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

# Example 1:
# Input: grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

# Example 2:
# Input: grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.


class Solution(object):
    def numEnclaves(self, grid):
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 1:
                return
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        if len(grid) < 3:
            return 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][m - 1] == 1:
                dfs(i, m - 1)

        for i in range(m):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[n - 1][i] == 1:
                dfs(n - 1, i)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        return count
