# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)
        stack.reverse()
        for c in t:
            if stack and c == stack[-1]:
                stack.pop()
        return not stack


def main() -> int:
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))
    return 0


if __name__ == '__main__':
    main()
