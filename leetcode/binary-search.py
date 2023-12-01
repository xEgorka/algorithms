# https://leetcode.com/problems/binary-search

# Use two pointers to check target against the middle element


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1


def main() -> int:
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))
    return 0


if __name__ == '__main__':
    main()
