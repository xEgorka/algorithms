# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array



from typing import List, Optional


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return


def main() -> int:
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin(nums))
    return 0


if __name__ == '__main__':
    main()
