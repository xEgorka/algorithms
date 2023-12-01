# https://leetcode.com/problems/balanced-binary-tree

# Recursively calculate left & rigth trees heights and whether they
# balanced, return if heights differ less than two and maximum height,
# don't forget to add one to height. There are two base cases: first,
# if no root, then the tree is balanced. Second, if either left or
# rigth is not balanced then the tree is not balanced.


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True, 0
            lb, lh = helper(root.left)
            rb, rh = helper(root.right)
            if not lb or not rb:
                return False, -1
            return abs(lh - rh) < 2, 1 + max(lh, rh)

        return helper(root)[0]


def main() -> int:
    print(Solution().isBalanced(root))
    return 0


if __name__ == '__main__':
    main()
