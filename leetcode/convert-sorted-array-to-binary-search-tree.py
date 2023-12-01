# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Take mid and assign to root, return root. Recursively assign left
# and right leafs


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left <= right:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = helper(left, mid - 1)
                root.right = helper(mid + 1, right)
                return root

        return helper(0, len(nums) - 1)


def main() -> int:
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))
    return 0


if __name__ == '__main__':
    main()
