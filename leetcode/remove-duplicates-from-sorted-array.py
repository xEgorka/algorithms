# https://leetcode.com/problems/remove-duplicates-from-sorted-array


from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        return j + 1


def main() -> int:
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
    return 0


if __name__ == '__main__':
    main()
