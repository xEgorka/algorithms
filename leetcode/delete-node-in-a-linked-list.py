# https://leetcode.com/problems/delete-node-in-a-linked-list

# Do not delete the object, just change value and pointer to next
# node


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def main() -> int:
    node = ListNode(4)
    print(Solution().deleteNode(node))
    return 0


if __name__ == '__main__':
    main()
