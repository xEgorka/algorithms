# https://leetcode.com/problems/binary-tree-paths

# Traverse by dfs, add currend node to path, if there are no leafs,
# append path to answer set and quit recursion.


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(root, path):
            path += str(root.val) + '->'
            if not root.left and not root.right:
                ans.append(path[:-2])
                return

            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)

        dfs(root, '')
        return ans


def main() -> int:
    root = TreeNode()
    print(Solution().binaryTreePaths(root))
    return 0


if __name__ == '__main__':
    main()
