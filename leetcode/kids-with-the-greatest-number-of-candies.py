# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

from typing import List, Optional


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= maxx:
                result.append(True)
            else:
                result.append(False)
        return result


def main() -> int:
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(Solution().kidsWithCandies(candies, extraCandies))
    return 0


if __name__ == '__main__':
    main()
