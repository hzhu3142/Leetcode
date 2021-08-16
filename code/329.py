class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            res = 0
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                if matrix[x][y] > matrix[i][j]:
                    res = max(res, dfs(x, y))

            dp[i][j] = 1 + res
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0

        dp = [[0] * n for i in range(m)]

        res = 0
        for x in range(m):
            for y in range(n):
                res = max(res, dfs(x, y))
        return res

