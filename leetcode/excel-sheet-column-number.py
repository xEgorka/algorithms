# https://leetcode.com/problems/excel-sheet-column-number

# Convert from base-26 positional numeral system to decimal. Add 1
# because Excel starts counting from 1


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
            'U': 20,
            'V': 21,
            'W': 22,
            'X': 23,
            'Y': 24,
            'Z': 25,
        }

        ans = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            ans += (d[columnTitle[i]] + 1) * 26 ** (len(columnTitle) - i - 1)
        return ans


def main() -> int:
    columnTitle = "AB"
    columnTitle = "ZY"
    columnTitle = "A"
    print(Solution().titleToNumber(columnTitle))
    return 0


if __name__ == '__main__':
    main()
