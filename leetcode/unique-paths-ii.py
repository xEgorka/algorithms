# https://leetcode.com/problems/unique-paths-ii

from typing import List, Optional


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


def main() -> int:
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
    return 0


if __name__ == '__main__':
    main()
