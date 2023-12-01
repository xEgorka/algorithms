# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

# Iterate haystack and check if needle equals haystack substring from
# the current position


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        lh = len(haystack)
        ln = len(needle)
        for i in range(lh - ln + 1):
            if haystack[i : i + ln] == needle:
                return i
        return -1


def main() -> int:
    haystack = "abc"
    needle = "c"
    print(Solution().strStr(haystack, needle))
    return 0


if __name__ == '__main__':
    main()
