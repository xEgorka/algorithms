# https://leetcode.com/problems/group-anagrams

from typing import List, Optional
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # d = {}
        # for s in strs:
        #     w = ''.join(sorted(s))
        #     if w not in d:
        #         d[w] = len(ans)
        #         ans.append([])
        #         ans[len(ans) - 1].append(s)
        #     else:
        #         ans[d[w]].append(s)
        # return ans

        ans = defaultdict(list)
        [ans[tuple(sorted(s))].append(s) for s in strs]
        return ans.values()


def main() -> int:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
    return 0


if __name__ == '__main__':
    main()
