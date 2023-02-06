def main() -> int:
    n, s, schedule = int(input()), [], []
    [s.append(list(map(float, input().split()))) for _ in range(n)]
    s.sort(key=lambda x: (x[1], x[0]))

    for i in range(n):
        if not i:
            schedule.append(s[0])
            end = s[0][1]
        else:
            if end <= s[i][0]:
                schedule.append(s[i])
                end = s[i][1]

    print(len(schedule))
    for x in schedule:
        if x[0].is_integer():
            x[0] = int(x[0])
        if x[1].is_integer():
            x[1] = int(x[1])
        print(*x)
    return 0


if __name__ == '__main__':
    main()
