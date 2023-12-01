# https://leetcode.com/problems/majority-element

# Use Counter to select most_common


from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


def main() -> int:
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
    return 0


if __name__ == '__main__':
    main()
