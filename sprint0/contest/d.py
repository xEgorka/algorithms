from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if target_sum == arr[i] + arr[j]:
                return [arr[i], arr[j]]
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


def main() -> int:
    arr, target_sum = read_input()
    print_result(two_sum(arr, target_sum))
    return 0


if __name__ == '__main__':
    main()
