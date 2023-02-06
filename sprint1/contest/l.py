def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter, longer = sorted(shorter), sorted(longer)
    for i in range(len(shorter)):
        left, right = i, -i - 1
        if shorter[left] != longer[left] and shorter[right] == longer[right]:
            return longer[left]
        if shorter[left] == longer[left] and shorter[right] != longer[right]:
            return longer[right]
        if shorter[left] != longer[left] and shorter[right] != longer[right]:
            return longer[left]
    return shorter[right]


def main() -> int:
    print(get_excessive_letter(input().strip(), input().strip()))
    return 0


if __name__ == '__main__':
    main()
