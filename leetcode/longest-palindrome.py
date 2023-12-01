# https://leetcode.com/problems/longest-palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1
        ans = 0
        for k, v in hash.items():
            cur = v - (v % 2)
            ans += cur
            hash[k] -= cur
        return ans if not sum(hash.values()) else ans + 1


def main() -> int:
    s = "abccccdd"
    print(Solution().longestPalindrome(s))
    return 0


if __name__ == '__main__':
    main()
