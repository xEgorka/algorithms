# https://leetcode.com/problems/swap-nodes-in-pairs

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        prev = dummy
        cur = head

        while cur and cur.next:
            nxt = cur.next

            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur

            prev = cur
            cur = cur.next
        return dummy.next


def main() -> int:
    head = ListNode()
    print(Solution().swapPairs(head))
    return 0


if __name__ == '__main__':
    main()
