class Stack:
    def __init__(self) -> None:
        self.items = []

    def check_sequence(self, item: str) -> None:
        if (
            (self.peek() == '{' and item == '}')
            or (self.peek() == '[' and item == ']')
            or (self.peek() == '(' and item == ')')
        ):
            self.items.pop()
        else:
            self.items.append(item)

    def peek(self) -> str:
        return self.items[-1] if len(self.items) else 'empty'

    def is_empty(self) -> bool:
        return True if not len(self.items) else False


def is_correct_bracket_seq(seq: str) -> bool:
    '''Checks if bracket sequence correct.'''

    stack = Stack()
    for symbol in seq:
        stack.check_sequence(symbol)
    return True if stack.is_empty() else False


def main() -> int:
    print(is_correct_bracket_seq(list(input())))
    return 0


if __name__ == '__main__':
    main()
