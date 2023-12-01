# https://leetcode.com/problems/spiral-matrix

from typing import List, Optional


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        m, n = len(matrix), len(matrix[0])
        ans = []

        r, c = 0, 0
        dirr = (0, 1)
        for _ in range(m * n):
            ans.append(matrix[r][c])
            matrix[r][c] = '#'
            rs, cs = dirr
            nr, nc = r + rs, c + cs
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#':
                r, c = nr, nc
            else:
                dirr = d[dirr]
                rs, cs = dirr
                r, c = r + rs, c + cs

        return ans


def main() -> int:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
    return 0


if __name__ == '__main__':
    main()
