# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Count nodes first. Iterate the list and delete the node


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        x = 0
        while node:
            x += 1
            node = node.next

        if x == 1:
            return None

        dummy = ListNode(None, head)
        prev = dummy
        curr = head
        i = 0
        m = x - (n + 1)
        while curr:
            i += 1
            if i == m:
                prev.next = curr.next
                return dummy.next
            prev = curr
            curr = curr.next


def main() -> int:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    new_head = Solution().removeNthFromEnd(head, n)
    node = new_head
    while node:
        print(node.val)
        node = node.next
    return 0


if __name__ == '__main__':
    main()
