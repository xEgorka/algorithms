# https://leetcode.com/problems/max-consecutive-ones

# DP, count each consecutive sequences, return max one


from typing import List, Optional


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i]:
                dp[i+1] = dp[i] + 1
            else:
                dp[i+1] = 0
        return max(dp)


def main() -> int:
    # nums = [1, 1, 0, 1, 1, 1]
    nums = [1, 0, 1, 1, 0, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
    return 0


if __name__ == '__main__':
    main()
