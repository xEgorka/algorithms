# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and left <= right:
                if s[left] != s[right]:
                    break
                if len(ans) < right - left + 1:
                    ans = s[left : right + 1]
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and left <= right:
                if s[left] != s[right]:
                    break
                if len(ans) < right - left + 1:
                    ans = s[left : right + 1]
                left -= 1
                right += 1

        return ans


def main() -> int:
    s = "babad"
    print(Solution().longestPalindrome(s))
    return 0


if __name__ == '__main__':
    main()
