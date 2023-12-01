# https://leetcode.com/problems/contains-duplicate-ii

# Use hash to store index for each seen num, check if current num was
# seen and distance between the indicies


from typing import List, Optional


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False


def main() -> int:
    nums = [1, 2, 3, 1]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))
    return 0


if __name__ == '__main__':
    main()
