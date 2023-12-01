# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# Use two pointers when nums sorted


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] == target:
                return list((left + 1, right + 1))
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1


def main() -> int:
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
    return 0


if __name__ == '__main__':
    main()
