# https://leetcode.com/problems/add-two-numbers

# Create third linked list using divmod, don't forget about carry


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        l3 = ListNode()
        node3 = l3
        carry = 0
        while node1 or node2:
            if node1 and node2:
                carry, node3.val = divmod((carry + node1.val + node2.val), 10)
            elif node1:
                carry, node3.val = divmod((carry + node1.val), 10)
            elif node2:
                carry, node3.val = divmod((carry + node2.val), 10)

            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
            if node1 or node2:
                node3.next = ListNode()
                node3 = node3.next

        if carry:
            node3.next = ListNode()
            node3 = node3.next
            node3.val = carry
        return l3


def main() -> int:
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    node = Solution().addTwoNumbers(l1, l2)

    ans=[]
    while node:
        ans.append(node.val)
        node = node.next
    print(*ans)
    return 0


if __name__ == '__main__':
    main()
