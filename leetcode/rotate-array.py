# https://leetcode.com/problems/rotate-array

from typing import List, Optional


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        rev(0, n - 1)
        rev(0, k % n - 1)
        rev(k % n, n - 1)

        return


def main() -> int:
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
    return 0


if __name__ == '__main__':
    main()
