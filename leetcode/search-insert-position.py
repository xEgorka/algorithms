# https://leetcode.com/problems/search-insert-position

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


# alternative solution
# return bisect.bisect_left(nums,target)


def main() -> int:
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))
    return 0


if __name__ == '__main__':
    main()
