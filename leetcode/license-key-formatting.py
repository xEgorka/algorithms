# https://leetcode.com/problems/license-key-formatting

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join([c.upper() for c in s if c.isalnum()])
        if not s:
            return ''
        first = len(s) % k
        ans = s[:first]
        for i in range(first, len(s), k):
            ans += '-' + s[i : i + k]
        return ans if ans[0] != '-' else ans[1:]


def main() -> int:
    s = "5F3Z-2e-9-w"
    k = 4
    print(Solution().licenseKeyFormatting(s, k))
    return 0


if __name__ == '__main__':
    main()
