# https://leetcode.com/problems/missing-number

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(len(nums) + 1)) - set(nums))[0]


def main() -> int:
    print(Solution().missingNumber([3, 0, 1]))
    return 0


if __name__ == '__main__':
    main()
