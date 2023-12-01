# https://leetcode.com/problems/guess-number-higher-or-lower

# Use binary search


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    if num == 6:
        return 0
    if num > 6:
        return -1
    return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right + left) // 2
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1


def main() -> int:
    n = 10
    print(Solution().guessNumber(n))
    return 0


if __name__ == '__main__':
    main()
