from typing import Any, List


class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        self.items.pop() if len(self.items) else print('error')

    def get_max(self) -> Any:
        print(max(self.items)) if len(self.items) else print('None')


def read_input() -> List[List[str]]:
    n = int(input())
    commands = []
    [commands.append(list(input().split())) for _ in range(n)]
    return commands


def write_output(commands: List[str]) -> None:
    stack = StackMax()
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
