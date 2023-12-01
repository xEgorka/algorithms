# https://leetcode.com/problems/set-matrix-zeroes

from typing import List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_col = False
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            if matrix[r][0] == 0:
                first_col = True
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0
        if first_col:
            for r in range(m):
                matrix[r][0] = 0


def main() -> int:
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(Solution().setZeroes(matrix))
    return 0


if __name__ == '__main__':
    main()
