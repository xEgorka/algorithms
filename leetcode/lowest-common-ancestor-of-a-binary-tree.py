# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        anc = {}
        parent = None
        stack = [(root, parent)]
        while stack:
            cur, parent = stack.pop()
            anc[cur] = parent
            if cur.left:
                stack.append((cur.left, cur))
            if cur.right:
                stack.append((cur.right, cur))

        p_anc = set()
        while p:
            p_anc.add(p)
            p = anc[p]

        while q not in p_anc:
            q = anc[q]

        return q


def main() -> int:
    print(Solution().lowestCommonAncestor(root, p, q))
    return 0


if __name__ == '__main__':
    main()
