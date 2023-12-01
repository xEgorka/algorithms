# https://leetcode.com/problems/ransom-note

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = Counter(magazine)
        for c in ransomNote:
            if c not in hash:
                return False
            elif not hash[c]:
                return False
            else:
                hash[c] -= 1
        return True


def main() -> int:
    ransomNote = "a"
    magazine = "b"
    print(Solution().canConstruct(ransomNote, magazine))
    return 0


if __name__ == '__main__':
    main()
