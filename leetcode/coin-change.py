# https://leetcode.com/problems/coin-change

# Recursion w/ memoisation. Each time there are n same subproblems,
# where n is number of coins. Take recursion, return number of coins and
# save result to memo, base cases are: amount eq zero, amount below
# zero, amount in memo.

# DP. Init dp table of length amount plus one with a big number. Base
# case dp0 is 0. Iterate amounts (dp), for each of denominations not
# greater than current amount apply the induction rule: take min of
# current amount and one plus dp of current amount minus current
# denomination. Return last dp if it is not the big number.


from typing import List, Optional


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}

        # def helper(amount):
        #     if not amount:
        #         return 0
        #     if amount < 0:
        #         return float('inf')
        #     if amount in memo:
        #         return memo[amount]
        #     ret = float('inf')
        #     for c in coins:
        #         ret = min(ret, 1 + helper(amount - c))
        #     memo[amount] = ret
        #     return ret

        # ans = helper(amount)
        # return ans if ans != float('inf') else -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[-1] if dp[-1] != float('inf') else -1


def main() -> int:
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
    return 0


if __name__ == '__main__':
    main()
