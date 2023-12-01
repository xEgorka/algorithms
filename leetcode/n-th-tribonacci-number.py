# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):
            dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
        return dp[-1]


def main() -> int:
    n = 4
    print(Solution().tribonacci(n))
    return 0


if __name__ == '__main__':
    main()
