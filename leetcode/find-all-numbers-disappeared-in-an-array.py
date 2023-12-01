# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

# Remove duplicates, compare to set to the full range set


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)


def main() -> int:
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
    return 0


if __name__ == '__main__':
    main()
