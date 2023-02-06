from typing import List


def get_max_score(k: int, draw: List[int]) -> None:
    players = 2
    k = k * players
    score = [0] * 10
    for i in range(16):
        if draw[i]:
            score[draw[i]] += 1
    print(sum(1 for x in score if x and x <= k in range(16)))


def main():
    k, draw = int(input()), []
    for i in range(4):
        draw += list(map(int, list(input().replace('.', '0'))))
    get_max_score(k, draw)


if __name__ == '__main__':
    main()
