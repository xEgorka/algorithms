# https://leetcode.com/problems/peak-index-in-a-mountain-array

# Use binary search


from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                left = mid
            else:
                right = mid


def main() -> int:
    arr = [0, 1, 0]
    print(Solution().peakIndexInMountainArray(arr))
    return 0


if __name__ == '__main__':
    main()
