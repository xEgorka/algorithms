# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            cur = stack.pop()
            if k - cur.val in seen:
                return True
            seen.add(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False


def main() -> int:
    root = TreeNode(
        5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))
    )
    k = 9
    print(Solution().findTarget(root, k))
    return 0


if __name__ == '__main__':
    main()
