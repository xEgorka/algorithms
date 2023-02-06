def get_longest_draw(n: int, seq: str) -> int:
    if n == 0 or n == 1:
        return 0

    x = 0
    prefix_sum = []
    for digit in seq:
        if int(digit) == 0:
            x -= 1
        else:
            x += 1
        prefix_sum.append(x)

    left, right = {}, {}
    for i, x in enumerate(prefix_sum):
        if x not in left:
            left[x] = i
        right[x] = i
    longest_draw = 0
    for key in left:
        longest_draw = max(longest_draw, right[key] - left[key])
    return longest_draw


def main() -> int:
    n = int(input())
    seq = '0' + str(input()).replace(' ', '')
    print(get_longest_draw(n, seq))
    return 0


if __name__ == '__main__':
    main()
