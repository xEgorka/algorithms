from typing import List


def is_first_object_less(object_1: List, object_2: List) -> bool:
    return (
        int(str(object_1) + str(object_2)) < int(str(object_2) + str(object_1))
    )


def insertion_sort(arr: List) -> None:
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and is_first_object_less(arr[j - 1], item_to_insert):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item_to_insert


def main() -> int:
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(arr)
    print(''.join(map(str, arr)))
    return 0


if __name__ == '__main__':
    main()
