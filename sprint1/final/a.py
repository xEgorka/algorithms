from typing import List


def find_closest_zero(n: int, houses: List[int]) -> None:
    zero = []
    [zero.append(i) for i in range(n) if not houses[i]]
    if len(zero) == 1:
        for i in range(n):
            houses[i] = abs(zero[0] - i)
        print(*houses)
        return
    for i in range(zero[0]):
        houses[i] = zero[0] - i
    for i in range(zero[-1], n):
        houses[i] = i - zero[-1]
    for i in range(len(zero) - 1):
        l = zero[i] + 1
        r = zero[i + 1] - 1
        cur_dist = 1
        while l <= r:
            houses[l] = houses[r] = cur_dist
            l += 1
            r -= 1
            cur_dist += 1
    print(*houses)


def main() -> int:
    find_closest_zero(int(input()), list(map(int, input().split())))
    return 0


if __name__ == '__main__':
    main()
