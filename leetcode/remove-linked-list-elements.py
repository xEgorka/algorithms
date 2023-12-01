# https://leetcode.com/problems/remove-linked-list-elements

# Iterate the list and perform removal


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = head
        prev = dummy
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next


def main() -> int:
    x = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=6)))
    Solution().removeElements(x, 6)
    return 0


if __name__ == '__main__':
    main()
