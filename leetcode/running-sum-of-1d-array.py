# https://leetcode.com/problems/running-sum-of-1d-array

from typing import List, Optional


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i]
        return dp


def main() -> int:
    nums = [1, 2, 3, 4]
    print(Solution().runningSum(nums))
    return 0


if __name__ == '__main__':
    main()
