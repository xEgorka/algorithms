# https://leetcode.com/problems/validate-binary-search-tree

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lo, hi):
            if not root:
                return True
            if not lo < root.val < hi:
                return False
            left = helper(root.left, lo, root.val)
            right = helper(root.right, root.val, hi)
            return left and right

        return helper(root, -float('inf'), float('inf'))


def main() -> int:
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().isValidBST(root))
    return 0


if __name__ == '__main__':
    main()
