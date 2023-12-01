# https://leetcode.com/problems/missing-ranges

from typing import List, Optional


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        n = len(nums)

        ans = []

        if not n:
            ans.append([lower, upper])
            return ans

        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            ans.append([nums[i] + 1, nums[i + 1] - 1])

        if upper > nums[n - 1]:
            ans.append([nums[n - 1] + 1, upper])

        return ans


def main() -> int:
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(Solution().findMissingRanges(nums, lower, upper))
    return 0


if __name__ == '__main__':
    main()
