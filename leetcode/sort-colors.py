# https://leetcode.com/problems/sort-colors

from typing import List, Optional


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, curr = 0, 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


def main() -> int:
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
    return 0


if __name__ == '__main__':
    main()
