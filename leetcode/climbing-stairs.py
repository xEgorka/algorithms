# https://leetcode.com/problems/climbing-stairs

# Each time you can either climb 1 or 2 steps hence cur ways equals
# cur - 1 plus cur - 2


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


def main() -> int:
    n = 3
    print(Solution().climbStairs(n))
    return 0


if __name__ == '__main__':
    main()
