# https://leetcode.com/problems/monotonic-array

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        inc, dec = True, True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dec = False
            if nums[i] > nums[i - 1]:
                inc = False
        return inc or dec


def main() -> int:
    nums = [1, 2, 2, 3]
    print(Solution().isMonotonic(nums))
    return 0


if __name__ == '__main__':
    main()
