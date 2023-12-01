# https://leetcode.com/problems/excel-sheet-column-title

# Convert from decimal to base-26 positional numeral system. Substract
# 1 because Excel starts counting from 1


class Solution:
    def convertToTitle(self, num: int) -> str:
        ans = ''
        while num > 0:
            num -= 1
            num, idx = divmod(num, 26)
            ans = chr(idx + 65) + ans
        return ans


def main() -> int:
    columnNumber = 26
    print(Solution().convertToTitle(columnNumber))
    return 0


if __name__ == '__main__':
    main()
