# https://leetcode.com/problems/word-break

# Check if the string begins with any of the words. If so, then
# recursively check the rest of the string. Use helper and lru_cache.
# Base case is empty string


from typing import List, Optional
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def helper(s):
            if not s:
                return True
            for w in wordDict:
                if w == s[: len(w)]:
                    if helper(s[len(w) :]):
                        return True
            return False

        return helper(s)


def main() -> int:
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
    return 0


if __name__ == '__main__':
    main()
