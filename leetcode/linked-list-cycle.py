# https://leetcode.com/problems/linked-list-cycle

# Use hash to check if cur node in seen


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


def main() -> int:
    head = ListNode()
    print(Solution().hasCycle(head))
    return 0


if __name__ == '__main__':
    main()
