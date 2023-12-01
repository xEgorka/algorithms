# https://leetcode.com/problems/invert-binary-tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root


# dfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root


def main() -> int:
    print(Solution().invertTree())
    return 0


if __name__ == '__main__':
    main()
