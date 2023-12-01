# https://leetcode.com/problems/range-sum-of-bst

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        left, right = 0, 0
        if root.val < high:
            right = self.rangeSumBST(root.right, low, high)
        if root.val > low:
            left = self.rangeSumBST(root.left, low, high)
        cur = root.val if low <= root.val <= high else 0
        return left + right + cur


def main() -> int:
    root = TreeNode(
        10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
    )
    low = 7
    high = 15
    print(Solution().rangeSumBST(root, low, high))
    return 0


if __name__ == '__main__':
    main()
