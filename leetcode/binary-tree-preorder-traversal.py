# https://leetcode.com/problems/binary-tree-preorder-traversal

# 1. Visit the root
# 2. Traverse the left subtree
# 3. Traverse the right subtree
# Preorder traversal is used to create a copy of the tree


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans


# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         return (
#             [root.val]
#             + self.preorderTraversal(root.left)
#             + self.preorderTraversal(root.right)
#             if root
#             else []
#         )


def main() -> int:
    root = TreeNode(4, TreeNode(6, TreeNode(2)), TreeNode(8))
    print(Solution().preorderTraversal(root))
    return 0


if __name__ == '__main__':
    main()
