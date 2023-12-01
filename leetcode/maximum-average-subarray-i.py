# https://leetcode.com/problems/maximum-average-subarray-i

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        cur_avg = cur_sum / k
        left, right = 0, k - 1
        while True:
            right += 1
            left += 1
            if right > len(nums) - 1:
                break
            cur_sum += nums[right]
            cur_sum -= nums[left - 1]
            cur_avg = max(cur_avg, cur_sum / k)
        return cur_avg


def main() -> int:
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    x = Solution().findMaxAverage(nums, k)
    print(x)
    return 0


if __name__ == '__main__':
    main()
