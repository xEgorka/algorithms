# https://leetcode.com/problems/move-zeroes

# Iterate nums with right pointer, swap elements if right is non-zero.
# So move non-zeroes to the beggining and zeroes to the end


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return


def main() -> int:
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))
    print(nums)
    return 0


if __name__ == '__main__':
    main()
