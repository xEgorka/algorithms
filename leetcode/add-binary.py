# https://leetcode.com/problems/add-binary

# Fill the shorter string with zeroes, sum digit by digit using
# divmod, don't forget check if carry, reverse ans string


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        if la > lb:
            b = (la - lb) * '0' + b
        else:
            a = (lb - la) * '0' + a

        carry, ans = 0, ''
        for i in range(len(a) - 1, -1, -1):
            d1 = int(a[i])
            d2 = int(b[i])
            carry, d = divmod(d1 + d2 + carry, 2)
            ans += str(d)
        if carry:
            ans += str(carry)
        return ans[::-1]


def main() -> int:
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))
    return 0


if __name__ == '__main__':
    main()
