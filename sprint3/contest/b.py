from typing import List


def combinations(seq: str, keyboard: dict, comb: List, n: int) -> None:
    if n == len(seq) - 1:
        comb.sort()
        print(*comb)
        return
    [comb.append(x) for x in keyboard[seq[0]]] if n == 0 else None
    new_comb = []
    [new_comb.append(x + y) for y in keyboard[seq[n + 1]] for x in comb]
    combinations(seq, keyboard, new_comb, n + 1)


def main() -> int:
    seq = str(input())
    keyboard = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    combinations(seq, keyboard, [], 0)
    return 0


if __name__ == '__main__':
    main()
