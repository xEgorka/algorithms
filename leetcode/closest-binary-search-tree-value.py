# https://leetcode.com/problems/closest-binary-search-tree-value

# DFS the tree, save closest to target val, return if it equals
# target, compare node to target to decide traverse direction


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, cur, target):
            if not node:
                return cur

            if cur == target:
                return cur

            if abs(node.val - target) < abs(cur - target):
                cur = node.val

            if target > node.val:
                kid = dfs(node.right, cur, target)
            else:
                kid = dfs(node.left, cur, target)

            return kid

        return dfs(root, float('inf'), target)


def main() -> int:
    print(Solution().closestValue(root, target))
    return 0


if __name__ == '__main__':
    main()
