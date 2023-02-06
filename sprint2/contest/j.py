from typing import Any, List


class Node:
    def __init__(self, value, next_item=None) -> None:
        self.value = value
        self.next_item = next_item


class MyNodeQueue:
    def __init__(self):
        self.cur_size = 0

    def is_empty(self) -> bool:
        return self.cur_size == 0

    def size(self) -> None:
        print(self.cur_size)

    def put(self, x: int) -> None:
        if self.is_empty():
            self.head = Node(x)
            self.tail = self.head
            self.cur_size = 1
        else:
            new_tail = Node(x)
            self.tail.next_item = new_tail
            self.tail = new_tail
            self.cur_size += 1

    def get(self) -> Any:
        if self.is_empty():
            print('error')
        else:
            print(self.head.value)
            self.head = self.head.next_item
            self.cur_size -= 1


def read_input() -> List[List[str]]:
    n = int(input())
    commands = []
    [commands.append(list(input().split())) for i in range(n)]
    return commands


def write_output(commands: List[str]) -> None:
    queue = MyNodeQueue()
    for command in commands:
        if command[0] == 'size':
            queue.size()
        elif command[0] == 'put':
            queue.put(command[1])
        else:
            queue.get()


def main() -> int:
    commands = read_input()
    write_output(commands)
    return 0


if __name__ == '__main__':
    main()
