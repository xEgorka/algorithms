def main() -> int:
    n = int(input())
    temperature = list(map(int, input().split()))
    m = int(input())
    pattern = list(map(int, input().split()))

    ans = []
    for i, t in enumerate(temperature):
        if i > n - m:
            break
        match = True
        for j in range(len(pattern)):
            if not j:
                c = pattern[j] - temperature[i + j]
            else:
                if c != pattern[j] - temperature[i + j]:
                    match = False
                    break
        if match:
            ans.append(i + 1)
    print(*ans)
    return 0


if __name__ == '__main__':
    main()
