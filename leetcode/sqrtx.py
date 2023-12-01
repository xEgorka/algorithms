# https://leetcode.com/problems/sqrtx


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            pivot = (left + right) // 2
            num = pivot * pivot
            if num == x:
                return pivot
            if num > x:
                right = pivot - 1
            else:
                left = pivot + 1
        return right


def main() -> int:
    x = 8
    x = 9
    print(Solution().mySqrt(x))
    return 0


if __name__ == '__main__':
    main()
