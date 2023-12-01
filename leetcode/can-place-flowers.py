# https://leetcode.com/problems/can-place-flowers

# Append dummy beds from both sides, iterate flowerbed starting from
# the second bed and pland the flower if there three empty beds in a
# row. Return if all the new flowers have been planted.


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


def main() -> int:
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))
    return 0


if __name__ == '__main__':
    main()
