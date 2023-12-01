# https://leetcode.com/problems/rotate-list

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        n = 0
        while node:
            n += 1
            node = node.next

        if n == 1:
            return head

        k = k % n

        if not k:
            return head

        node = head
        for i in range(n - 1):
            if i == n - 1 - k:
                cut = node
            node = node.next

        new_head = cut.next
        cut.next = None
        node.next = head

        return new_head


def main() -> int:
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode(1, ListNode(2))

    k = 2
    # print(Solution().rotateRight(head, k))
    head = Solution().rotateRight(head, k)
    while head:
        print(head.val)
        head = head.next
    return 0


if __name__ == '__main__':
    main()
