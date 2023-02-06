class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> int:
    stack = []
    stack.append(root)
    cur_max = root.value
    while len(stack):
        node = stack.pop()
        cur_max = max(cur_max, node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return cur_max


def main() -> int:
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3
    return 0


if __name__ == '__main__':
    main()
