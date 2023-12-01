# https://leetcode.com/problems/squares-of-a-sorted-array

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                ans.append(nums[right] * nums[right])
                right -= 1
            else:
                ans.append(nums[left] * nums[left])
                left += 1
        return ans[::-1]


def main() -> int:
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
    return 0


if __name__ == '__main__':
    main()
