# https://leetcode.com/problems/remove-duplicates-from-sorted-list

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)
        prev = dummy
        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next


def main() -> int:
    head = ListNode(1, ListNode(1, ListNode(2)))
    new_head = Solution().deleteDuplicates(head)
    cur = new_head
    while cur:
        print(cur.val)
        cur = cur.next
    return 0


if __name__ == '__main__':
    main()
