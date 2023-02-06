def main() -> int:
    s, n = input(), int(input())
    hash = {}
    for _ in range(n):
        t, k = list(input().split())
        hash[int(k)] = t
    ans = ''
    for i in range(len(s)):
        if i in hash:
            ans += hash[i] + s[i]
        else:
            ans += s[i]
    if len(s) in hash:
        ans += hash[len(s)]
    print(ans)
    return 0


if __name__ == '__main__':
    main()
