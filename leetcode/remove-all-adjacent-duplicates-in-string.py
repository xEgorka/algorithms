# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

# Filter adjacent duplicates using stack


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


def main() -> int:
    s = "abbaca"
    print(Solution().removeDuplicates(s))
    return 0


if __name__ == '__main__':
    main()
