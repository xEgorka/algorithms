# https://leetcode.com/problems/check-if-n-and-its-double-exist

# Iterate array and check if cur * 2 or cur / 2 was seen. Add cur to
# seen


from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False


def main() -> int:
    arr = [10, 2, 5, 3]
    print(Solution().checkIfExist(arr))
    return 0


if __name__ == '__main__':
    main()
