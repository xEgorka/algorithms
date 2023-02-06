def get_weather_randomness(temps):
    if len(temps) == 1:
        print(1)
        return
    rand = 0
    right = temps[1] < temps[0]
    if right:
        rand += 1
    for i in range(1, len(temps)):
        if temps[i - 1] != temps[i]:
            left = not (right)
        else:
            left = False
        if i == len(temps) - 1:
            if left:
                rand += 1
            print(rand)
            return
        right = temps[i + 1] < temps[i]
        if left and right:
            rand += 1


def main():
    _ = int(input())
    get_weather_randomness(list(map(int, input().strip().split())))


if __name__ == '__main__':
    main()
