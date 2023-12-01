# https://leetcode.com/problems/search-in-rotated-sorted-array-ii


from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return False if nums[0] != target else True

        l, r = 0, len(nums) - 1

        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


def main() -> int:
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))
    return 0


if __name__ == '__main__':
    main()
