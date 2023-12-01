# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# Iterate prices, updade min price if current price less than min
# price, else update max profit if current profit more than max profit


from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        # for i in range(len(prices)):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     elif prices[i] - min_price > max_profit:
        #         max_profit = prices[i] - min_price

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit


def main() -> int:
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
    return 0


if __name__ == '__main__':
    main()
