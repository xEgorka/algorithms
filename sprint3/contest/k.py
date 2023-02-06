from typing import List


def merge(arr: List, left: int, mid: int, right: int) -> List:
    left = arr[left:mid]
    right = arr[mid:right]

    result = [0] * len(arr)
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def merge_sort(arr: List, left: int, right: int) -> None:
    if right - left == 1:
        return
    merge_sort(arr, left, left + (right - left) // 2)
    merge_sort(arr, left + (right - left) // 2, right)
    arr[left:right] = merge(arr[left:right], 0, (right - left) // 2, right - left)


def main() -> int:
    # arr=[4,5,3,0, 1,2]
    # print(*arr)
    # merge_sort(arr, 0, 4)
    # print(*arr)
    # assert arr==[0,3,4,5, 1,2]

    # a = [1, 4, 9,   2, 10, 11]
    # b = merge(a, 0, 3, 6)
    # print(*b)
    # expected = [1, 2, 4, 9, 10, 11]
    # print(*expected)
    # assert b == expected

    # a = [3,0]
    # b = merge(a, 0, 1, 2)
    # print(*b)
    # expected = [1, 2, 4, 9, 10, 11]
    # assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    assert c == [1, 1, 2, 2, 4, 10]
    return 0


if __name__ == '__main__':
    main()
