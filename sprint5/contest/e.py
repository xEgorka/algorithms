class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    return is_BST(root, float('-inf'), float('inf'))


def is_BST(node, min, max):
    if node is None:
        return True

    if node.value < min or node.value > max:
        return False

    return is_BST(node.left, min, node.value - 1) and is_BST(
        node.right, node.value + 1, max
    )


def main() -> int:
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)
    return 0


if __name__ == '__main__':
    main()
