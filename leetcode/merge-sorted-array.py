# https://leetcode.com/problems/merge-sorted-array

from typing import List, Optional


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        while k >= 0:
            if n < 1 or (m > 0 and nums1[m - 1] > nums2[n - 1]):
                nums1[k] = nums1[m - 1]
                m -= 1
            else:
                nums1[k] = nums2[n - 1]
                n -= 1
            k -= 1
        return


def main() -> int:
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(*nums1)
    return 0


if __name__ == '__main__':
    main()
