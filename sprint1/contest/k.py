from typing import List


def get_sum(number_list: List[int], k: int) -> List[int]:
    first_number = number_list
    second_number = [int(x) for x in str(k)]

    sum = []
    cur_sum = 0

    for i in range(max(len(first_number), len(second_number))):
        first = first_number[-i - 1] if i < len(first_number) else 0
        second = second_number[-i - 1] if i < len(second_number) else 0
        x = first + second + cur_sum
        if x < 10:
            sum.append(x)
            cur_sum = 0
        else:
            sum.append(int(str(x)[-1]))
            cur_sum = int(str(x)[0])
    if cur_sum > 0:
        sum.append(cur_sum)
    sum.reverse()
    return sum


def main():
    _ = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    print(' '.join(map(str, get_sum(number_list, k))))


if __name__ == '__main__':
    main()
