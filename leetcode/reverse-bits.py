# https://leetcode.com/problems/reverse-bits

# Bitwise operator & gives 1 if both bits are 1, << left shift
# operator removes left bits

# The key idea is that for a bit that is situated at the index i,
# after the reversion, its position should be 31-i (note: the index
# starts from zero)

# We iterate through the bit string of the input integer, from right
# to left (i.e. n = n >> 1). To retrieve the right-most bit of an
# integer, we apply the bit AND operation (n & 1)


class Solution:
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


def main() -> int:
    n = 43261596
    print(Solution().reverseBits(n))
    return 0


if __name__ == '__main__':
    main()
