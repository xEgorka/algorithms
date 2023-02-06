def main() -> int:
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    if n == 1 and k == 1:
        print(*arr)
        return

    s1, s2 = [], []
    cur_sum1, cur_sum2 = 0, 0

    for i in range(len(arr)):
        cur_sum1 += arr[i]
        cur_sum2 += arr[len(arr) - 1 - i]
        s1.append(cur_sum1)
        s2.append(cur_sum2)

    cur_sum = s1[k - 1]
    for i in range(1, k):
        cur_sum = max(cur_sum, s1[k - 1 - i] + s2[i - 1])
    cur_sum = max(cur_sum, s2[k - 1])
    print(cur_sum)


if __name__ == '__main__':
    main()
