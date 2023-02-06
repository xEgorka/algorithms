def evaluate_function(a, b, c, x):
    print(a * x * x + b * x + c)


def main():
    a, x, b, c = map(int, input().strip().split())
    evaluate_function(a, b, c, x)


if __name__ == '__main__':
    main()
