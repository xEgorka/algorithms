# https://leetcode.com/problems/unique-paths

from functools import lru_cache


# class Solution:
#     @lru_cache(None)
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 1 or n == 1:
#             return 1
#         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                    continue
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]


def main() -> int:
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))
    return 0


if __name__ == '__main__':
    main()
