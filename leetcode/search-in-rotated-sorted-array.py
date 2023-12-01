# https://leetcode.com/problems/search-in-rotated-sorted-array

# If a sorted array is shifted, if you take the middle, always one side
# will be sorted. Take the recursion according to that rule


from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]:  # Left side of mid is sorted
                if nums[l] <= target and target < nums[mid]:  # Target in the left side
                    r = mid - 1
                else:  # in right side
                    l = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target and target <= nums[r]:  # Target in the right side
                    l = mid + 1
                else:  # in left side
                    r = mid - 1
        return -1


def main() -> int:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(Solution().search(nums, target))
    return 0


if __name__ == '__main__':
    main()
