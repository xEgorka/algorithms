# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit * digit
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


def main() -> int:
    n = 19
    print(Solution().isHappy(n))
    return 0


if __name__ == '__main__':
    main()
