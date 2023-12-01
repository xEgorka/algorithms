# https://leetcode.com/problems/counting-bits

# Bitwise operator & gives 1 if both bits are 1, >> rigth shift
# operator removes rigth bits


from typing import List, Optional


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            cur = 0
            while i:
                cur += i & 1
                i >>= 1
            ans.append(cur)
        return ans


def main() -> int:
    print(Solution().countBits(3))
    return 0


if __name__ == '__main__':
    main()
