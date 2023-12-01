# https://leetcode.com/problems/container-with-most-water

# Use two pointers, save max area every step. Move pointer which has
# smaller height. You have two heights H_left and H_right, and H_right <
# H_left, then we know we have two choices, we want to move one of them.
# If we move the larger one, we cannot increase the height for the
# simple reason that we are always limited by the shortest, and we would
# be decreasing j-i, the width as well


from typing import List, Optional


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left <= right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


def main() -> int:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
    return 0


if __name__ == '__main__':
    main()
