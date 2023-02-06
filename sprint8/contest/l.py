def prefix_function(s: str) -> None:
    π = [0] * len(s)
    for i in range(1, len(s)):
        k = π[i - 1]
        while k and s[k] != s[i]:
            k = π[k - 1]
        if s[k] == s[i]:
            k += 1
        π[i] = k
    print(*π)


def main() -> int:
    prefix_function(input())
    return 0


if __name__ == '__main__':
    main()
