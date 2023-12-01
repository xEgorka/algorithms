# https://leetcode.com/problems/merge-two-sorted-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(None)
        prev = dummy

        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next
            prev = prev.next
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return dummy.next


def main() -> int:
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    cur = Solution().mergeTwoLists(list1, list2)
    while cur:
        print(cur.val)
        cur = cur.next
    return 0


if __name__ == '__main__':
    main()
