# https://leetcode.com/problems/binary-tree-postorder-traversal

# 1. Traverse the left subtree
# 2. Traverse the right subtree
# 3. Visit the root
# Postorder traversal is used to delete the tree


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                ans.append(node.val)

        helper(root)
        return ans


def main() -> int:
    root = TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))
    print(Solution().postorderTraversal(root))
    return 0


if __name__ == '__main__':
    main()


# все зависит от того, когда забирать текущий нод
# preorder
def helper(node):
    if node:
        ans.append(node.val)
        helper(node.left)
        helper(node.right)


# inorder
def helper(node):
    if node:
        helper(node.left)
        ans.append(node.val)
        helper(node.right)
