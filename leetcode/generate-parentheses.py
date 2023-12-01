# https://leetcode.com/problems/generate-parentheses

# Generate all combinations of parentheses, filter well-formed ones
# using stack


from typing import List, Optional


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n: int, seq: str) -> None:
            if n == 0:
                stack = []
                for p in seq:
                    if len(stack) and stack[-1] == '(' and p == ')':
                        stack.pop()
                    else:
                        stack.append(p)
                if not len(stack):
                    ans.append(seq)
            else:
                helper(n - 1, seq + '(')
                helper(n - 1, seq + ')')

        ans = []
        helper(n * 2, '')

        return ans


def main() -> int:
    n = 3
    print(Solution().generateParenthesis(n))
    return 0


if __name__ == '__main__':
    main()
