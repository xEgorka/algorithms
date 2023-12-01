# https://leetcode.com/problems/single-number

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


def main() -> int:
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
    return 0


if __name__ == '__main__':
    main()
