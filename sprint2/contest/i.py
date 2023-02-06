from typing import Any, List, Tuple


class MyQueueSized:
    '''Sized Queue'''

    def __init__(self, max_size) -> None:
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.cur_size = 0

    def is_empty(self) -> bool:
        return self.cur_size == 0

    def peek(self):
        print(self.queue[self.head]) if not self.is_empty() else print('None')

    def size(self) -> int:
        print(self.cur_size)

    def push(self, x: int) -> Any:
        if self.cur_size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.cur_size += 1
        else:
            print('error')

    def pop(self) -> Any:
        if self.is_empty():
            print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.cur_size -= 1
            print(x)


def read_input() -> Tuple[int, List[List[str]]]:
    n = int(input())
    max_size = int(input())
    commands = []
    for _ in range(n):
        commands.append(list(input().split()))
    return max_size, commands


def write_output(max_size, commands: List[str]) -> None:
    queue = MyQueueSized(max_size)
    for command in commands:
        if command[0] == 'size':
            queue.size()
        elif command[0] == 'push':
            queue.push(int(command[1]))
        elif command[0] == 'peek':
            queue.peek()
        else:
            queue.pop()


def main() -> int:
    max_size, commands = read_input()
    write_output(max_size, commands)
    return 0


if __name__ == '__main__':
    main()
