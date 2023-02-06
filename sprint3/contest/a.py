class Stack:
    def __init__(self) -> None:
        self.items = []

    def check_sequence(self, item: str) -> None:
        if self.peek() == '(' and item == ')':
            self.items.pop()
        else:
            self.items.append(item)

    def peek(self) -> str:
        return self.items[-1] if len(self.items) else 'empty'

    def is_empty(self) -> bool:
        return True if not len(self.items) else False


def is_correct_bracket_seq(string: str) -> bool:
    '''Checks if bracket sequence correct.'''

    stack = Stack()
    for symbol in string:
        stack.check_sequence(symbol)
    return True if stack.is_empty() else False


def gen_paren(n: int, seq: str) -> None:
    '''Generates possible bracket sequences and prints correct ones.'''

    if n == 0:
        if is_correct_bracket_seq(seq):
            print(seq)
    else:
        gen_paren(n - 1, seq + '(')
        gen_paren(n - 1, seq + ')')


def main() -> int:
    n = int(input())
    gen_paren(2 * n, '')
    return 0


if __name__ == '__main__':
    main()
