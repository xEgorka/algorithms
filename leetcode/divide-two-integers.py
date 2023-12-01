# https://leetcode.com/problems/divide-two-integers


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []
        powers_of_two = []

        power_of_two = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powers_of_two.append(power_of_two)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor
            power_of_two += power_of_two

        # Go from largest double to smallest, checking if the current double fits
        # into the remainder of the dividend
        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                # If it does fit, add the current power_of_two to the quotient
                quotient += powers_of_two[i]
                # Update dividend to take into account the bit we've now removed.
                dividend -= doubles[i]

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive
        return quotient if negatives != 1 else -quotient


def main() -> int:
    dividend = 100
    divisor = 3
    print(Solution().divide(dividend, divisor))
    return 0


if __name__ == '__main__':
    main()
