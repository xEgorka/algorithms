# https://leetcode.com/problems/product-of-array-except-self

from typing import List, Optional


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_left = [1] * len(nums)
        nums_right = [1] * len(nums)
        for i in range(1, len(nums)):
            nums_left[i] = nums_left[i - 1] * nums[i - 1]
            nums_right[len(nums) - 1 - i] = (
                nums_right[len(nums) - 1 - i + 1] * nums[len(nums) - 1 - i + 1]
            )
        ans = []
        for i in range(len(nums)):
            ans.append(nums_left[i] * nums_right[i])
        return ans


def main() -> int:
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
    return 0


if __name__ == '__main__':
    main()
