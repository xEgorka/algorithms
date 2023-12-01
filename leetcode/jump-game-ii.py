# https://leetcode.com/problems/jump-game-ii

from typing import List, Optional
from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i):
            if i >= len(nums) - 1:
                return 0

            ans = float('inf')

            for j in range(1, nums[i] + 1):
                ans = min(ans, 1 + helper(i + j))
            return ans

        return helper(0)


def main() -> int:
    nums = [2, 3, 0, 1, 4]
    print(Solution().jump(nums))
    return 0


if __name__ == '__main__':
    main()
