from typing import List


def bubble_sort(arr: List) -> None:
    for j in range(len(arr) - 1):
        f = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f += 1
        if not f and not j:
            print(*arr)
            break
        elif not f:
            break
        else:
            print(*arr)


def main() -> int:
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)
    return 0


if __name__ == '__main__':
    main()
