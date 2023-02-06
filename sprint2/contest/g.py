from typing import List


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return 'error'


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.stack_max_item = Stack()

    def push(self, item: int) -> None:
        if self.stack_max_item.peek() == 'error':
            self.stack_max_item.push(item)
        elif item >= self.stack_max_item.peek():
            self.stack_max_item.push(item)
        self.items.append(item)

    def pop(self):
        if len(self.items):
            if self.items[-1] == self.stack_max_item.peek():
                self.stack_max_item.pop()
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if len(self.items):
            print(self.stack_max_item.peek())
        else:
            print('None')


def read_input() -> List[List[str]]:
    n = int(input())
    commands = []
    [commands.append(list(input().split())) for _ in range(n)]
    return commands


def write_output(commands: List[str]) -> None:
    stack = StackMaxEffective()
    for command in commands:
        if command[0] == 'get_max':
            stack.get_max()
        elif command[0] == 'push':
            stack.push(int(command[1]))
        else:
            stack.pop()


def main() -> int:
    commands = read_input()
    write_output(commands)
    return 0


if __name__ == '__main__':
    main()
