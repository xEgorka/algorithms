# https://leetcode.com/problems/search-in-a-binary-search-tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)


def main() -> int:
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    val = 2

    cur = Solution().searchBST(root, val)
    stack = [cur]

    while stack:
        cur = stack.pop()
        print(cur.val, end=' ')
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return 0


if __name__ == '__main__':
    main()
