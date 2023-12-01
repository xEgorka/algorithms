# https://leetcode.com/problems/valid-mountain-array

# Iterate from the left and search for peak, same from the right.
# Check if peak the same in case peaks were found


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i, j = 0, len(arr) - 1
        while arr[i] < arr[i + 1]:
            i += 1
            if i > len(arr) - 2:
                return False
        while arr[j] < arr[j - 1]:
            j -= 1
            if j < 1:
                return False
        return i == j


def main() -> int:
    arr = [3, 5, 4]
    print(Solution().validMountainArray(arr))
    return 0


if __name__ == '__main__':
    main()
