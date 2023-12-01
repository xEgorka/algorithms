# https://leetcode.com/problems/reverse-integer

# Make the num positive. Take last digit and add it to result x10,
# repeat until num


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x *= sign
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        return rev if rev >= -(2**31) and rev <= (2**31 - 1) else 0


def main() -> int:
    x = 123
    print(Solution().reverse(x))
    return 0


if __name__ == '__main__':
    main()
