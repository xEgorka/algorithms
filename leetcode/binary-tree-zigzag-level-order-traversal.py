# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# BFS the tree using queue, append level values to answer set, reverse
# level every other time


from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        ans, direction = [], False

        while q:
            level = [node.val for node in q]
            if direction:
                level.reverse()
            ans.append(level)
            direction = not direction

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans


def main() -> int:
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().zigzagLevelOrder(root))
    return 0


if __name__ == '__main__':
    main()
