# https://leetcode.com/problems/contains-duplicate

# Make set, compare len set versus len array


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def main() -> int:
    print(Solution().containsDuplicate([1, 2, 3, 1]))
    return 0


if __name__ == '__main__':
    main()
