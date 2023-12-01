# https://leetcode.com/problems/remove-element

# Keep two pointers i and j, where i is the slow-runner while j is the
# fast-runner. Copy fast to slow in case fast val is not target, so
# the task is move all not target to the right


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


def main() -> int:
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val))
    print(nums)
    return 0


if __name__ == '__main__':
    main()
