# https://leetcode.com/problems/pascals-triangle

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1, 1]]

        # base case
        if numRows < 3:
            return dp[:numRows]

        for _ in range(numRows - 2):
            next_row = [1]
            for i in range(1, len(dp[-1])):
                next_row.append(dp[-1][i] + dp[-1][i - 1])
            next_row += [1]
            dp.append(next_row)
        return dp


def main() -> int:
    numRows = 5
    print(Solution().generate(numRows))
    return 0


if __name__ == '__main__':
    main()
