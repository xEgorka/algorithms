# https://leetcode.com/problems/verifying-an-alien-dictionary

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        hash = {}
        for i, c in enumerate(order):
            hash[c] = i

        for i in range(1, len(words)):
            n = min(len(words[i - 1]), len(words[i]))
            if words[i - 1][:n] == words[i] and len(words[i]) < len(words[i - 1]):
                return False
            for j in range(n):
                if hash[words[i - 1][j]] < hash[words[i][j]]:
                    break
                if hash[words[i - 1][j]] > hash[words[i][j]]:
                    return False
        return True


def main() -> int:
    # words = ["hello", "leetcode"]
    # order = "hlabcdefgijkmnopqrstuvwxyz"
    # words = ["word", "world", "row"]
    # order = "worldabcefghijkmnpqstuvxyz"
    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))
    return 0


if __name__ == '__main__':
    main()
