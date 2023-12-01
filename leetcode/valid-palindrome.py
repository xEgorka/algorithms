# https://leetcode.com/problems/valid-palindrome

# Two pointers to check


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         a = {
#             'a',
#             'b',
#             'c',
#             'd',
#             'e',
#             'f',
#             'g',
#             'h',
#             'i',
#             'j',
#             'k',
#             'l',
#             'm',
#             'n',
#             'o',
#             'p',
#             'q',
#             'r',
#             's',
#             't',
#             'u',
#             'v',
#             'w',
#             'x',
#             'y',
#             'z',
#             '1',
#             '2',
#             '3',
#             '4',
#             '5',
#             '6',
#             '7',
#             '8',
#             '9',
#             '0',
#         }
#         t = ''
#         for c in s:
#             if c in a:
#                 t += c
#         return t == t[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


def main() -> int:
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
    return 0


if __name__ == '__main__':
    main()
