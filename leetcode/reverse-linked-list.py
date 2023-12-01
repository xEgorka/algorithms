# https://leetcode.com/problems/reverse-linked-list

# Swap cur.next, prev and cur with prev, cur and cur.next


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


def main() -> int:
    head = ListNode()
    print(Solution().reverseList(head))
    return 0


if __name__ == '__main__':
    main()
