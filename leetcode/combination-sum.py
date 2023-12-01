# https://leetcode.com/problems/combination-sum

# DFS tree of all possible combinations, candidate may repeat. Iterate
# candidates, decrease target, increase combination ever step. Base
# cases: target eq zero, target below zero. Save combination when
# target eq zero.


from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, target, comb):
            if not target:
                ans.append(comb)
                return

            if target < 0:
                return

            for j in range(i, len(candidates)):
                dfs(j, target - candidates[j], comb + [candidates[j]])

        dfs(0, target, [])
        return ans


def main() -> int:
    # candidates = [2, 3, 6, 7]
    # target = 7
    candidates = [1]
    target = 10

    print(Solution().combinationSum(candidates, target))
    return 0


if __name__ == '__main__':
    main()
