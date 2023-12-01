# https://leetcode.com/problems/backspace-string-compare

# Use stack to pop backspace chars after that compare the strings


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []
        for c in s:
            if s1 and c == '#':
                s1.pop()
                continue
            elif c != '#':
                s1.append(c)
        for c in t:
            if s2 and c == '#':
                s2.pop()
                continue
            elif c != '#':
                s2.append(c)
        return s1 == s2


def main() -> int:
    s = "y#fo##f"
    t = "y#f#o##f"
    print(Solution().backspaceCompare(s, t))
    return 0


if __name__ == '__main__':
    main()
