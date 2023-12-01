# https://leetcode.com/problems/first-bad-version

# Just binary search


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


def main() -> int:
    print(Solution().firstBadVersion(n))
    return 0


if __name__ == '__main__':
    main()
