# https://leetcode.com/problems/subsets

from typing import List, Optional


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, subset):
            ans.append(subset)
            if i < len(nums):
                for j in range(i, len(nums)):
                    dfs(j + 1, subset + [nums[j]])
        dfs(0,[])

        return ans


def main() -> int:
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    return 0


if __name__ == '__main__':
    main()
