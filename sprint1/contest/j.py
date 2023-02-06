from typing import List


def factorize(number: int) -> List[int]:
    i, cur_number, factors = 2, number, []
    while number > i * i:
        if cur_number % i == 0:
            factors.append(i)
            cur_number //= i
            continue
        i += 1 if i == 2 else 2
    factors.append(cur_number) if cur_number > 1 else None
    return factors


def main():
    print(*factorize(int(input())))


if __name__ == '__main__':
    main()
