# https://leetcode.com/problems/fibonacci-number

# Cur equals sum prev two. Take care of dp len


class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


def main() -> int:
    n = 4
    print(Solution().fib(n))
    return 0


if __name__ == '__main__':
    main()
