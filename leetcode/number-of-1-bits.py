# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans


def main() -> int:
    n = 0b00000000000000000000000000001011
    print(Solution().hammingWeight(n))
    return 0


if __name__ == '__main__':
    main()
