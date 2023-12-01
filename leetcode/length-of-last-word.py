# https://leetcode.com/problems/length-of-last-word

# Simple iterate from the end of the string


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                ans += 1
            elif s[i] == ' ' and ans:
                break
        return ans


def main() -> int:
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
    return 0


if __name__ == '__main__':
    main()
