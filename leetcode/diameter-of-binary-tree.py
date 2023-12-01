# https://leetcode.com/problems/diameter-of-binary-tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = -float('inf')

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        helper(root)
        return self.ans


def main() -> int:
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().diameterOfBinaryTree(root))
    return 0


if __name__ == '__main__':
    main()
