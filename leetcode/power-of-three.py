# https://leetcode.com/problems/power-of-three

# Divide by three while there is no remainder. If got 1, then true,
# else false


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1


def main() -> int:
    print(Solution().isPowerOfThree(27))
    return 0


if __name__ == '__main__':
    main()
