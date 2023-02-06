from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    cur_sum = sum(arr[0:window_size])
    cur_avg = cur_sum / window_size
    result.append(cur_avg)
    for i in range(0, len(arr) - window_size):
        cur_sum -= arr[i]
        cur_sum += arr[i + window_size]
        cur_avg = cur_sum / window_size
        result.append(cur_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


def main() -> int:
    arr, window_size = read_input()
    print(" ".join(map(str, moving_average(arr, window_size))))
    return 0


if __name__ == '__main__':
    main()
