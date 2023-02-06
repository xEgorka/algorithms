from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    result = []
    for element in range(0, len(a)):
        result = result + [a[element], b[element]]
    return result


def read_input() -> Tuple[List[int], List[int]]:
    _ = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


def main() -> int:
    a, b = read_input()
    print(" ".join(map(str, zipper(a, b))))
    return 0


if __name__ == '__main__':
    main()
