from typing import List


def binary_search(arr: List[int], x: int, left: int, right: int) -> int:
    if arr[right] < x:
        return -1
    if right - left <= 1:
        if arr[left] >= x:
            return left + 1
        else:
            return right + 1
    mid = (left + right) // 2
    if x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def main() -> int:
    right = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    print(
        *[
            binary_search(arr, s, left=0, right=len(arr) - 1),
            binary_search(arr, s * 2, left=0, right=len(arr) - 1),
        ]
    )
    return 0


if __name__ == '__main__':
    main()
