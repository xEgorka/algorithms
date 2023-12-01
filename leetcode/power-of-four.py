# https://leetcode.com/problems/power-of-four

# Divide by four recursively. If got 1, then true, if got less than 1,
# then false


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfFour(n / 4)


def main() -> int:
    print(Solution().isPowerOfFour(64))
    return 0


if __name__ == '__main__':
    main()
