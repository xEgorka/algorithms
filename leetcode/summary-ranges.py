# https://leetcode.com/problems/summary-ranges

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = nums[0]
        nums += [float('inf')]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                e = nums[i - 1]
                if s == e:
                    ans.append(str(s))
                else:
                    ans.append(f'{s}->{e}')
                s = nums[i]
        return ans


def main() -> int:
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))
    return 0


if __name__ == '__main__':
    main()
