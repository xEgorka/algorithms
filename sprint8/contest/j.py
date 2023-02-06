from typing import List


class Node:
    def __init__(self) -> None:
        self.transition = {}
        self.is_terminal = False


def split_camel_case(name: str) -> List[str]:
    split, word = [], ''
    for x in name:
        if x.isupper() and len(word):
            split.append(word)
            word = ''
        word += x
    split.append(word)
    return split


def add_string(root: Node, string: str) -> None:
    current_node = root
    for i in range(len(string)):
        symbol = string[i]
        if symbol not in current_node.transition:
            new_node = Node()
            current_node.transition[symbol] = new_node
        current_node = current_node.transition[symbol]
    current_node.is_terminal = True


def main() -> int:
    n = int(input())
    root = Node()
    [add_string(root, split_camel_case(input())) for _ in range(n)]
    print(root.transition)
    return 0


if __name__ == '__main__':
    main()
