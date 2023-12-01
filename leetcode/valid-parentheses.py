# https://leetcode.com/problems/valid-parentheses

# Use stack to check


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return not stack


def main() -> int:
    s = "()[]{}"
    print(Solution().isValid(s))
    return 0


if __name__ == '__main__':
    main()
