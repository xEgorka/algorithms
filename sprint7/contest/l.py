def main() -> int:
    n, M = list(map(int, input().split()))
    weight = list(map(int, list(input().split())))
    if not M:
        print(0)
        return
    dp = [False] * (M + 1)
    for w in weight:
        stack = []
        for i in range(1, M + 1):
            if not dp[i] and i - w > 0:
                if dp[i - w]:
                    stack.append(i)
        if w < M:
            dp[w] = True
        while len(stack):
            dp[stack.pop()] = True
    for i in range(M):
        if dp[M - i]:
            print(M - i)
            return
    return 0


if __name__ == '__main__':
    main()
