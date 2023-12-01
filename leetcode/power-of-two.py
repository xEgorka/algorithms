# https://leetcode.com/problems/power-of-two

# Divide by two recursively. If got 1, then true, if got less than 1,
# then false


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfTwo(n / 2)


def main() -> int:
    print(Solution().isPowerOfTwo(4))
    return 0


if __name__ == '__main__':
    main()
