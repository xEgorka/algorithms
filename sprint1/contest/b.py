def check_parity(a, b, c):
    return (True if a & 1 and b & 1 and c & 1 else False) or (
        True if not (a & 1) and not (b & 1) and not (c & 1) else False
    )


def main():
    a, b, c = map(int, input().strip().split())
    if check_parity(a, b, c):
        print('WIN')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
