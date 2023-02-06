# -- ПРИНЦИП РАБОТЫ --

# Хэш-таблица закодирована на основе стандартного списка с разрешением
# коллизий методом цепочек. Поддерживает только целочисленные ключи и
# значения, количество ключей не больше 10^5. Не поддерживает
# рехэширование и масштабирование.

# Доступны следующие операции:

# put key value —– добавление пары ключ-значение. Если заданный ключ уже
# есть в таблице, то соответствующее ему значение обновляется.

# get key –— получение значения по ключу. Если ключа нет в таблице, то
# выводится «None». Иначе выводится найденное значение.

# delete key –— удаление ключа из таблицы. Если такого ключа нет, то
# выводится «None», иначе выводится хранимое по данному ключу значение и
# ключ помечается как удаленный, физическое удаление не выполняется.

# Значение количества корзин M = 40111 подобрано с учётом специфики
# задачи и имеющихся ресурсов. Если параметр меньше, возникнет много
# коллизий, операции выполняются дольше лимита по времени. Если
# параметр больше — лимит памяти будет исчерпан.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Хэш-табли́ца — это структура данных, реализующая интерфейс
# ассоциативного массива, то есть позволяет хранить пары ключ-значение
# и выполнять три операции: добавление новой пары, поиск и удаление
# пары по ключу.

# Реализованная структура данных попадает под определение хэш-таблицы.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Сложность операций добавления, поиска и удаления одинаковая, так как
# узкое место каждой из задач — поиск элемента в цепочке. В худшем
# случае возможно попадание всех элементов в одну корзину что приведет
# к выполнению операций за O(N). В среднем же операции выполняются за
# O(1).


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# Выполнение операций не требует дополнительной памяти.


# https://contest.yandex.ru/contest/24414/run-report/75183697/
class LinkedList:
    def __init__(self, key: int = None, value: int = None, next: int = None) -> None:
        self.key, self.value = key, value
        self.next, self.deleted = next, False


class HashTable:
    def __init__(self) -> None:
        self.M = 40111
        self.table = [LinkedList()] * self.M

    def search(self, key: int) -> LinkedList:
        node = self.table[key % self.M]
        while node:
            if node.key == key:
                return node
            node = node.next

    def get(self, key: int) -> None:
        node = self.search(key)
        if node and not node.deleted:
            print(node.value)
        else:
            print('None')

    def put(self, key: int, value: int) -> None:
        node = self.search(key)
        if node:
            node.value, node.deleted = value, False
        else:
            idx = key % self.M
            self.table[idx] = LinkedList(key, value, self.table[idx])

    def delete(self, key: int) -> None:
        node = self.search(key)
        if node and not node.deleted:
            print(node.value)
            node.deleted = True
        else:
            print('None')


def main() -> int:
    h = HashTable()
    n = int(input())
    for _ in range(n):
        cmd = list(input().split())
        if cmd[0] == 'get':
            h.get(int(cmd[1]))
        elif cmd[0] == 'put':
            h.put(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'delete':
            h.delete(int(cmd[1]))
    return 0


if __name__ == '__main__':
    main()
