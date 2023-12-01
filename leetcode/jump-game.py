# https://leetcode.com/problems/jump-game

from typing import List, Optional


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


def main() -> int:
    nums = [2, 3, 1, 1, 4]
    print(Solution().canJump(nums))
    return 0


if __name__ == '__main__':
    main()
