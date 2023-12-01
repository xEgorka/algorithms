# https://leetcode.com/problems/assign-cookies

# Sort children and cookies, iterate through the cookies and increment
# the answer if cookie greater or equal than greedy factor, check if
# there more kids


from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for c in s:
            if c >= g[i]:
                i += 1
            if i == len(g):
                break
        return i


def main() -> int:
    g = [1, 2, 3]  # children
    s = [1, 1]  # cookies
    print(Solution().findContentChildren(g, s))
    return 0


if __name__ == '__main__':
    main()
