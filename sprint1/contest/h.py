def get_sum(first_number: str, second_number: str) -> str:
    sum = ''
    cur_sum = 0
    for i in range(0, max(len(first_number), len(second_number))):
        if i < len(first_number):
            first = first_number[-i - 1]
        else:
            first = '0'
        if i < len(second_number):
            second = second_number[-i - 1]
        else:
            second = '0'

        if (int(first) + int(second) + cur_sum) == 0:
            sum = '0' + sum
            cur_sum = 0
        elif (int(first) + int(second) + cur_sum) == 1:
            sum = '1' + sum
            cur_sum = 0
        elif (int(first) + int(second) + cur_sum) == 2:
            sum = '0' + sum
            cur_sum = 1
        elif (int(first) + int(second) + cur_sum) == 3:
            sum = '1' + sum
            cur_sum = 1

    if cur_sum == 1:
        sum = '1' + sum
    return sum


def main() -> int:
    print(get_sum(input().strip(), input().strip()))
    return 0


if __name__ == '__main__':
    main()
