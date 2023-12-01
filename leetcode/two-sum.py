# https://leetcode.com/problems/two-sum

# Use hash to store index of seen nums, check if target - num among
# seen nums


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return list((i, seen[comp]))
            seen[num] = i


def main() -> int:
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
    return 0


if __name__ == '__main__':
    main()
