# https://leetcode.com/problems/intersection-of-two-linked-lists

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        n1 = 0
        cur = headA
        while cur:
            n1 += 1
            cur = cur.next
        n2 = 0
        cur = headB
        while cur:
            n2 += 1
            cur = cur.next

        if n1 > n2:
            delta = n1 - n2
            cur_long = headA
            cur_short = headB
        else:
            delta = n2 - n1
            cur_long = headB
            cur_short = headA

        while delta:
            cur_long = cur_long.next
            delta -= 1

        while cur_long:
            if cur_long == cur_short:
                return cur_long
            cur_long = cur_long.next
            cur_short = cur_short.next


def main() -> int:
    print(Solution().getIntersectionNode(headA, headB))
    return 0


if __name__ == '__main__':
    main()
