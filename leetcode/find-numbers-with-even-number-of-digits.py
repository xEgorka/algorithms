# https://leetcode.com/problems/find-numbers-with-even-number-of-digits

# Count digits in each num, increase ans only in even case


from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            d = 0
            while num:
                num //= 10
                d += 1
            ans += 0 if d % 2 else 1
        return ans


def main() -> int:
    nums = [12, 345, 2, 6, 7896]
    print(Solution().findNumbers(nums))
    return 0


if __name__ == '__main__':
    main()
