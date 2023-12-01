# https://leetcode.com/problems/3sum

# Use 2sum hash and outer cycle for third item, avoid dublicates among
# the triplets


from typing import List, Optional


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def two_sum(i):
            target = -nums[i]
            seen = set()
            for j in range(len(nums)):
                if i != j:
                    comp = target - nums[j]
                    if comp in seen:
                        ans.add(tuple(sorted([nums[i], nums[j], comp])))
                    seen.add(nums[j])

        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                two_sum(i)
        return ans


def main() -> int:
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
    return 0


if __name__ == '__main__':
    main()
