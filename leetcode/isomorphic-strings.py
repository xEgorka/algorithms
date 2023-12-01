# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] not in d1:
                if t[i] in d2 and d2[t[i]] !=s[i]:
                    return False
                else:
                    d1[s[i]] = t[i]
                    d2[t[i]] = s[i]
            else:
                if d1[s[i]] != t[i]:
                    return False
        return True


def main() -> int:
    s = "egg"
    t = "add"
    print(Solution().isIsomorphic(s, t))
    return 0


if __name__ == '__main__':
    main()
