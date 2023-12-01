# https://leetcode.com/problems/copy-list-with-random-pointer

# Copy linked list, make hash map old to new node objects. Iterate the
# old list second time and update random pointer in the new list


from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        d = {}

        dummy = Node(0)
        prev = dummy
        cur = head

        while cur:
            new = Node(cur.val)
            d[cur] = new

            prev.next = new
            prev = new
            cur = cur.next

        cur_old = head
        cur_new = dummy.next

        while cur_old:
            cur_new.random = d[cur_old.random] if cur_old.random else None
            cur_old = cur_old.next
            cur_new = cur_new.next

        return dummy.next


def main() -> int:
    print(Solution().copyRandomList(head))
    return 0


if __name__ == '__main__':
    main()
