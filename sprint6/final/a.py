# -- ПРИНЦИП РАБОТЫ --

# Поиск остовного дерева по алгоритму Прима. В множество вершин
# остовного дерева добавляется случайная стартовая вершина из связного
# графа. Среди инцидентных ребер стартовой вершины осуществляется
# поиск ребра с первоприоритетным весом. Поиск ребра выполняется с
# помощью приоритетной очереди, имплементированной на основе кучи.
# Если вершина, в которую ведет найденное ребро, еще не добавлена в
# остовное дерево, то найденное ребро принадлежит остовному дереву, а
# для рассматриваемой вершины повторяются действия выполненные над
# стартовой вершиной до тех пор, пока в множестве вершин остовного
# дерева не окажутся все вершины исходного связного графа.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Дан неориентированный, возможно несвязный граф, в котором могут быть
# петли и кратные ребра. По условию задачи требуется вывести вес
# максимального остовного дерева, если оно существует, иначе (если в
# графе несколько компонент связности) вывести фразу «Oops! I did it
# again».

# Иными словами, требуется отыскать одно из остовных деревьев графа и,
# если оно единственное, то вывести суммарный вес ребер остовного
# дерева, при этом первоприоритетными являются ребра с максимальным
# весом, поэтому куча поддерживает максимум. Вес найденного ребра,
# принадлежащего остовному дереву, прибавляется к суммарному весу
# остовного дерева. При считывании графа для кратных ребер выбирается
# единственное с максимальным весом.

# Если в цикле действий закончились ребра для рассмотрения, а в
# множестве вершин остовного дерева оказались не все вершины исходного
# графа, значит в графе несколько компонент связности. Такой результат
# обрабатывается исключительно с печатью требуемой фразы. Программа
# завершает работу штатно выводом суммарного веса остовного дерева.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Благодаря приоритетной очереди сложность алгоритма Прима O(E⋅logV),
# где E — количество рёбер в графе, а V — количество вершин.


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Для хранения ребер остовного дерева потребуется O(E) памяти, для
# множества вершин остовного дерева еще O(V). Суммарно программа
# потребляет O(E + V).


# https://contest.yandex.ru/contest/25070/run-report/75201411/
from typing import List


class Heap:
    def __init__(self) -> None:
        self.heap = [-1]

    def compare(self, obj_1: List[int], obj_2: List[int]) -> bool:
        return obj_1[2] < obj_2[2]

    def heap_add(self, key: List[int]) -> None:
        self.heap.append(key)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, idx: int) -> int:
        if idx == 1:
            return idx
        if self.compare(self.heap[idx // 2], self.heap[idx]):
            self.heap[idx // 2], self.heap[idx] = (
                self.heap[idx],
                self.heap[idx // 2],
            )
            idx = self.sift_up(idx // 2)
        return idx

    def pop_max_prior(self) -> List[int]:
        max_prior_key, self.heap[1] = (
            self.heap[1],
            self.heap[len(self.heap) - 1],
        )
        self.heap.pop()
        self.sift_down(1)
        return max_prior_key

    def sift_down(self, idx: int) -> int:
        if len(self.heap) - 1 == 1:
            return idx
        l, r = 2 * idx, 2 * idx + 1
        if len(self.heap) - 1 < l:
            return idx
        if r <= len(self.heap) - 1 and self.compare(self.heap[l], self.heap[r]):
            idx_max_prior = r
        else:
            idx_max_prior = l
        if self.compare(self.heap[idx], self.heap[idx_max_prior]):
            self.heap[idx], self.heap[idx_max_prior] = (
                self.heap[idx_max_prior],
                self.heap[idx],
            )
            idx = self.sift_down(idx_max_prior)
        return idx


class GraphNotConnected(Exception):
    pass


class Graph:
    def __init__(self, n) -> None:
        self.n, self.adj = n, {}
        for i in range(n):
            self.adj[i] = {}

    def create_edge(self, v: int, u: int, w: int) -> None:
        u, v = u - 1, v - 1
        if v not in self.adj[u] or (v in self.adj[u] and self.adj[u][v] < w):
            self.adj[u][v] = w
        if u not in self.adj[v] or (u in self.adj[v] and self.adj[v][u] < w):
            self.adj[v][u] = w

    def add_vertex(self, v: int) -> None:
        self.not_added.remove(v)
        for u in self.adj[v].keys():
            if u in self.not_added:
                self.edges.heap_add([v, u, self.adj[v][u]])

    def find_MST(self) -> None:
        self.not_added = set()
        self.edges = Heap()
        mst_weight = 0
        [self.not_added.add(i) for i in range(self.n)]
        self.add_vertex(0)
        while len(self.not_added) and len(self.edges.heap) - 1:
            e = self.edges.pop_max_prior()
            if e[1] in self.not_added:
                mst_weight += e[2]
                self.add_vertex(e[1])
        try:
            if len(self.not_added):
                raise GraphNotConnected
        except GraphNotConnected:
            print('Oops! I did it again')
        else:
            print(mst_weight)


def main() -> int:
    n, m = list(map(int, input().split()))
    G = Graph(n)
    [G.create_edge(*list(map(int, input().split()))) for _ in range(m)]
    G.find_MST()
    return 0


if __name__ == '__main__':
    main()
