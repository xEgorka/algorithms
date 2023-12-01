# https://leetcode.com/problems/sum-of-left-leaves

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, None)]
        ans = 0
        while stack:
            cur, is_left = stack.pop()
            if not cur.left and not cur.right and is_left:
                ans += cur.val
            if cur.left:
                stack.append((cur.left, 1))
            if cur.right:
                stack.append((cur.right, 0))
        return ans

# recursive
# class Solution:
#     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#         def dfs(node, left):
#             if not node:
#                 return 0
#             if not node.left and not node.right and left:
#                 return node.val
#             left = dfs(node.left, True)
#             right = dfs(node.right, False)
#             return left + right
#         return dfs(root, False)


def main() -> int:
    root = TreeNode
    print(Solution().sumOfLeftLeaves(root))
    return 0


if __name__ == '__main__':
    main()
