# https://leetcode.com/problems/merge-two-sorted-lists

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next


def main() -> int:
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    head = Solution().mergeTwoLists(list1, list2)
    while head:
        print(head.val)
        head = head.next
    return 0


if __name__ == '__main__':
    main()
