class Node:
    def __init__(self, value, next_item=None) -> None:
        self.value = value
        self.next_item = next_item


def get_node_by_index(node: Node, index: int) -> Node:
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node: Node, idx: int) -> Node:
    if idx == 0:
        node = node.next_item
        return node
    current_node = get_node_by_index(node, idx)
    previous_node = get_node_by_index(node, idx - 1)
    if current_node.next_item is None:
        previous_node.next_item = None
    else:
        previous_node.next_item = current_node.next_item
    return node


def main() -> int:
    node2 = Node('node2', None)
    node1 = Node('node1', node2)
    node0 = Node('node0', node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is None
    return 0


if __name__ == '__main__':
    main()
