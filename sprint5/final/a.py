# -- ПРИНЦИП РАБОТЫ --

# Сортировка таблицы результатов участников соревнования выполняется
# по алгоритму сортировки кучей (Heapsort) c использованием
# дополнительной памяти. Программа сортирует массив по возрастанию.
# Для возможности непосредственного сравнения результатов отдельных
# участников между собой запись с результатом перед считыванием в
# оперативную память трансформируется в вид [-P, F, login].


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# По условию задачи требуется реализовать алгоритм сортировки кучей
# (англ. Heapsort) для таблицы результатов и при этом имплементировать
# собственную кучу. Требования соблюдены, за основу взяты задачи
# просеивание вверх и вниз.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Сложность сортировки кучей в худшем случае O(nlogn).


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Алгоритм использует дополнительную память для отсортированного массива
# на что расходует О(n) памяти.

# В сортировке кучей глубина рекурсии равна logn, поэтому
# этот метод расходует O(logn) + О(logn) = O(logn) памяти на стеке.


# https://contest.yandex.ru/contest/24810/run-report/70747085/
from typing import Any, List


def heap_add(heap: List[Any], key: int) -> None:
    heap.append(key)
    sift_up(heap, len(heap) - 1)


def sift_up(heap: List[Any], idx: int) -> int:
    if idx == 1:
        return idx
    if heap[idx // 2] > heap[idx]:
        heap[idx // 2], heap[idx] = heap[idx], heap[idx // 2]
        idx = sift_up(heap, idx // 2)
    return idx


def pop_max_prior(heap: List[Any]) -> Any:
    max_prior_key, heap[1] = heap[1], heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return max_prior_key


def sift_down(heap: List[Any], idx: int) -> int:
    if len(heap) - 1 == 1:
        return idx
    l, r = 2 * idx, 2 * idx + 1
    if len(heap) - 1 < l:
        return idx
    idx_max_prior = r if r <= len(heap) - 1 and heap[l] > heap[r] else l
    if heap[idx] > heap[idx_max_prior]:
        heap[idx], heap[idx_max_prior] = heap[idx_max_prior], heap[idx]
        idx = sift_down(heap, idx_max_prior)
    return idx


def heapsort(arr: List[Any]) -> List[Any]:
    heap, arr_sorted = [-1], []
    [heap_add(heap, key) for key in arr]
    [arr_sorted.append(pop_max_prior(heap)) for _ in range(len(heap) - 1)]
    return arr_sorted


def main() -> int:
    n, results = int(input()), []
    for _ in range(n):
        x = input().split()
        results.append([-int(x[1]), int(x[2]), x[0]])
    [print(x[2]) for x in heapsort(results)]
    return 0


if __name__ == '__main__':
    main()
