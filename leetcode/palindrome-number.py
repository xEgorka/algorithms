# https://leetcode.com/problems/palindrome-number

# Calculate reverse number using divmod, compare to original to detect
# a palindrome


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new = 0
        orig = x
        while x:
            x, d = divmod(x, 10)
            new = new * 10 + d
        return new == orig


def main() -> int:
    print(Solution().isPalindrome(121))
    return 0


if __name__ == '__main__':
    main()
