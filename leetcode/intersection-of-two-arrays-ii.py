# https://leetcode.com/problems/intersection-of-two-arrays-ii

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1) & Counter(nums2)
        ans = []
        for k, v in c.items():
            for _ in range(v):
                ans.append(k)
        return ans


def main() -> int:
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersect(nums1, nums2))
    return 0


if __name__ == '__main__':
    main()
