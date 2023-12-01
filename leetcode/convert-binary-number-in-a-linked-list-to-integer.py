# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Doubling method. Take previous and double it, add current. Start
# from zero:
# = 1
# = (1x2 + 0)
# = (1x2 + 0)x2  + 1
# = 1x2x2 + 0x2  + 1
# = 1x2²  + 0x2¹ + 2⁰
# = 5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = head.val + ans * 2
            head = head.next
        return ans


def main() -> int:
    head = ListNode(1, ListNode(0, ListNode(1)))
    print(Solution().getDecimalValue(head))
    return 0


if __name__ == '__main__':
    main()
