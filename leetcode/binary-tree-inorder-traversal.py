# https://leetcode.com/problems/binary-tree-inorder-traversal

# 1. Traverse the left subtree
# 2. Visit the root
# 3. Traverse the right subtree
# Inorder traversal gives nodes in non-decreasing order


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


def main() -> int:
    print(Solution().inorderTraversal(root))
    return 0


if __name__ == '__main__':
    main()
