# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        while len(s):
            if s[0] == ' ':
                s = s[1:]
            else:
                break
        if not len(s):
            return 0

        sign = '+'
        if s[0] == '-' or s[0] == '+':
            sign = s[0]
            s = s[1:]

        ans = ''
        while len(s):
            if s[0].isdigit():
                ans += s[0]
                s = s[1:]
            else:
                break
        if not len(ans):
            return 0

        ans = int(ans)
        if sign == '-':
            ans *= -1

        if ans < -(2**31):
            ans = -(2**31)

        if ans > 2**31 - 1:
            ans = 2**31 - 1

        return ans


def main() -> int:
    s = "   -4193 with words"
    print(Solution().myAtoi(s))
    return 0


if __name__ == '__main__':
    main()
