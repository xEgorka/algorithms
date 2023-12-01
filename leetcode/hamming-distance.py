# https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            ans += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return ans


def main() -> int:
    x, y = 1, 4
    print(Solution().hammingDistance(x, y))
    return 0


if __name__ == '__main__':
    main()
