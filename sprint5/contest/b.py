class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def count_h(node, h, arr):
    if not node.left or not node.right:
        arr.append(h)
    if node.left:
        count_h(node.left, h + 1, arr)
    if node.right:
        count_h(node.right, h + 1, arr)


def solution(root):
    arr = []
    count_h(root, 0, arr)
    if len(arr) == 1:
        arr.append(0)
    return max(arr) - min(arr) <= 1


def main() -> int:
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)
    return 0


if __name__ == '__main__':
    main()
