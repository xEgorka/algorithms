# https://leetcode.com/problems/sort-array-by-parity

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


def main() -> int:
    nums = [3, 1, 2, 4]
    print(Solution().sortArrayByParity(nums))
    return 0


if __name__ == '__main__':
    main()
