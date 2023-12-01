# https://leetcode.com/problems/valid-anagram

# Make two hashes and compare them


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def main() -> int:
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
    return 0


if __name__ == '__main__':
    main()
