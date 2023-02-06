def sift_down(heap, idx):
    size = len(heap) - 1
    if size == 1:
        return idx
    left = 2 * idx
    right = 2 * idx + 1
    if size < left:
        return idx
    if right <= size and heap[left] < heap[right]:
        idx_max = right
    else:
        idx_max = left
    if heap[idx] < heap[idx_max]:
        heap[idx], heap[idx_max] = heap[idx_max], heap[idx]
        idx = sift_down(heap, idx_max)
    return idx


def main() -> int:
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5
    return 0


if __name__ == '__main__':
    main()
