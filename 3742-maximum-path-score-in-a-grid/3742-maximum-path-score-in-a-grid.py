from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == -1:
                        continue
                    for di, dj in [(0, 1), (1, 0)]:
                        ni, nj = i + di, j + dj
                        if ni < m and nj < n:
                            val = grid[ni][nj]
                            cost = 1 if val in (1, 2) else 0
                            score = val 
                            if c + cost <= k:
                                dp[ni][nj][c + cost] = max(
                                    dp[ni][nj][c + cost],
                                    dp[i][j][c] + score
                                )
        res = max(dp[m-1][n-1])
        return res if res != -1 else -1