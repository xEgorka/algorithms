# https://leetcode.com/problems/letter-combinations-of-a-phone-number

from typing import List, Optional


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return ''

        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ans = []

        def dfs(i, comb):
            if i == len(digits):
                ans.append(comb)
                return

            for l in d[digits[i]]:
                dfs(i + 1, comb + l)

        dfs(0, '')

        return ans


def main() -> int:
    digits = "23"
    print(Solution().letterCombinations(digits))
    return 0


if __name__ == '__main__':
    main()
