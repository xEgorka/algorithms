# https://leetcode.com/problems/jewels-and-stones

# Use hash


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash = set(jewels)
        ans = 0
        for s in stones:
            if s in hash:
                ans += 1
        return ans


def main() -> int:
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))
    return 0


if __name__ == '__main__':
    main()
