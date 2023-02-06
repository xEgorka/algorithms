from typing import List


def is_first_object_less(object_1: List, object_2: List) -> bool:
    if object_1[0] < object_2[0]:
        return True
    elif object_1[0] == object_2[0] and object_1[1] < object_2[1]:
        return True
    else:
        return False


def insertion_sort(arr: List) -> None:
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and is_first_object_less(item_to_insert, arr[j - 1]):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item_to_insert


def merge(arr: List) -> None:
    i = 0
    j = 1
    result = []
    while i < len(arr) and j < len(arr):
        if arr[i][1] >= arr[j][0] and arr[i][1] <= arr[j][1]:
            arr[i][1] = arr[j][1]
            j += 1
        else:
            result.append(arr[i])
            i = j
            j += 2
    if i == len(arr) - 1 and result[len(result) - 1][1] < arr[i][0]:
        result.append(arr[i])
    return result


def main() -> int:
    n = int(input())
    arr = []
    [arr.append(list(map(int, input().split()))) for _ in range(n)]
    print(*arr)
    insertion_sort(arr)
    print(*arr)
    result = merge(arr)
    [print(*i) for i in result]
    return 0


if __name__ == '__main__':
    main()
