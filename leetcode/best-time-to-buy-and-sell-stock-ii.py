# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

# Starting from second price iterate prices and increase profit by
# prices delta if current price greater than previous one


from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans


def main() -> int:
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
    return 0


if __name__ == '__main__':
    main()
