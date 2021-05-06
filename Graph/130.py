# 130. Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
#                 ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# Output: [["X", "X", "X", "X"], ["X", "X", "X", "X"],
#          ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]


class Solution(object):
    def solve(self, board):
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != 'O':
                return
            board[i][j] = '*'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        if len(board) < 2:
            return board

        n = len(board)
        m = len(board[0])

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m - 1] == 'O':
                dfs(i, m - 1)

        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[n - 1][i] == 'O':
                dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'

        return board
