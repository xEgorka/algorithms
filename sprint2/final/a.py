# -- ПРИНЦИП РАБОТЫ --

# Дек закодирован с использованием кольцевого буфера. Указатели начала
# и конца очереди указывают на свободный для записи индекс. Индекс
# всегда находится в пределе от 0 до максимального количества
# элементов минус 1.

# Элементы могут быть добавлены в начало или в конец очереди. Элементы
# могут быть удалены из начала или из конца очереди. Добавление
# элемента в начало смещает указатель против часовой стрелки.
# Добавление элемента в конец смещает указатель по часовой стрелке.

# Удаление элемента смещает указатель в обратном направлении
# соответственно. Если элемент добавлен в пустую очередь, смещаются
# оба указателя. Если удален единственный элемент из очереди,
# смещаются оба указателя.

# Дек не позволяет добавить элемент при наличии максимального
# количества элементов. Дек не позволяет удалить элемент если
# элементов в очереди нет.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Дек - это интерфейс, который позволяет и добавлять, и извлекать
# элементы с обоих концов. Такой интерфейс называют «дек» (англ. deque
# — double ended queue, «очередь с двумя концами»). Дек можно
# воспринимать как двустороннюю очередь. Очередь работает по принципу
# FIFO.

# Описание алгоритма соответствует определению.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Добавление и удаление в любой из концов очереди стоит O(1).


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Дек занимает O(n) памяти, где n - максимальное количество элементов.


# https://contest.yandex.ru/contest/22781/run-report/75199581/
class DequeIsEmpty(Exception):
    '''Raised when deque is empty.'''

    pass


class DequeIsFull(Exception):
    '''Raised when deque is full.'''

    pass


class Deque:
    '''Sized deque (double ended queue) implementation.'''

    def __init__(self, max_size: int) -> None:
        self.deque = [None] * max_size
        self.max_n = max_size
        self.front = 0
        self.back = 0
        self.n = 0

    def is_full(self) -> bool:
        return self.n == self.max_n

    def is_empty(self) -> bool:
        return self.n == 0

    def shift_pointer(self, pointer: int) -> int:
        return pointer % self.max_n

    def push_back(self, value: int) -> None:
        try:
            if self.is_full():
                raise DequeIsFull
        except DequeIsFull:
            print('error')
        else:
            self.deque[self.back] = value
            self.back = self.shift_pointer(self.back + 1)
            if self.is_empty():
                self.front = self.shift_pointer(self.front - 1)
            self.n += 1

    def pop_back(self) -> None:
        try:
            if self.is_empty():
                raise DequeIsEmpty
        except DequeIsEmpty:
            print('error')
        else:
            print(self.deque[self.shift_pointer(self.back - 1)])
            self.back = self.shift_pointer(self.back - 1)
            self.n -= 1
            if self.is_empty():
                self.front = self.shift_pointer(self.front + 1)

    def push_front(self, value: int) -> None:
        try:
            if self.is_full():
                raise DequeIsFull
        except DequeIsFull:
            print('error')
        else:
            self.deque[self.front] = value
            self.front = self.shift_pointer(self.front - 1)
            if self.is_empty():
                self.back = self.shift_pointer(self.back + 1)
            self.n += 1

    def pop_front(self) -> None:
        try:
            if self.is_empty():
                raise DequeIsEmpty
        except DequeIsEmpty:
            print('error')
        else:
            print(self.deque[self.shift_pointer(self.front + 1)])
            self.front = self.shift_pointer(self.front + 1)
            self.n -= 1
            if self.is_empty():
                self.back = self.shift_pointer(self.back - 1)


def main() -> int:
    n = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push_back':
            deque.push_back(int(cmd[1]))
        elif cmd[0] == 'pop_back':
            deque.pop_back()
        elif cmd[0] == 'push_front':
            deque.push_front(int(cmd[1]))
        elif cmd[0] == 'pop_front':
            deque.pop_front()
    return 0


if __name__ == '__main__':
    main()
