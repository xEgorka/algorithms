# https://leetcode.com/problems/longest-continuous-increasing-subsequence

from typing import List, Optional


# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         left, right = 0, 1
#         cur_max = 0
#         while right <= len(nums) - 1:
#             if nums[right] > nums[right - 1]:
#                 cur_max = max((right - left + 1), cur_max)
#                 right += 1
#             else:
#                 left = right
#                 right += 1
#         return cur_max if cur_max else 1


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


def main() -> int:
    nums = [1, 3, 5, 4, 7]
    print(Solution().findLengthOfLCIS(nums))
    return 0


if __name__ == '__main__':
    main()
