# https://leetcode.com/problems/intersection-of-two-arrays

from collections import Counter
from typing import List, Optional


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # cnt1 = Counter(nums1)
        # cnt2 = Counter(nums2)
        # return cnt1 & cnt2
        return list(set(nums1) & set(nums2))


def main() -> int:
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersection(nums1, nums2))
    return 0


if __name__ == '__main__':
    main()
