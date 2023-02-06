# -- ПРИНЦИП РАБОТЫ --

# Проблема разбиения текста на слова из словаря решается методом
# динамического программирования.

# 1. Массив dp размером длины текста T, в ячейке dp[i] хранится ответ
# на вопрос: можно ли получить текст длиной i из слов словаря?
# 2. Базовый случай dp[0] = True.
# 3. Рекуррентная формула dp[i] = True, если dp[i-k] = True и T[i-k:i]
# = word, где word является рассматриваемым словом словаря длины k.
# 4. Массив dp заполняется по возрастанию индекса.
# 5. Ответ на искомый вопрос располагается в ячейке dp[n], где n -
# длина T.


# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

# Существует текст длиной i составленный из слов словаря тогда и
# только тогда, когда существует текст длиной i - k составленный из
# слов словаря, а также в словаре существует слово длиной k. По
# условию задачи слово может встречаться в разбиении текста T
# произвольное число раз.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --

# Программа требует О(n·m), где n - длина текста, m - количество слов
# в словаре. Такой алгоритм не укладывается в отведённое время,
# поэтому для снижения затрат условие наличия слова в словаре
# проверяется с помощью префиксного дерева вместо полного перебора по
# словарю. Поскольку по условию задачи можно использовать не все слова
# для разбиения, это серьёзно экономит время.

# В худшем случае затраты О(n·M), где n - длина текста, M = max mᵢ -
# длина самого длинного из слов словаря, при условии хранения
# переходов в массиве размером алфавита. На построение бора
# дополнительно расходуется O(L), где L - суммарная длина слов
# словаря.


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

# На хранение префиксного дерева расходуется О(L·∣∑∣), где L - суммарная
# длина слов словаря, ∣∑∣ - мощность алфавита возможных символов. Для
# массива dp выделяется память O(n), где n - длина текста.


# https://contest.yandex.ru/contest/26133/run-report/75031069/
class Node:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_terminal = False


class TextSplitter:
    def __init__(self) -> None:
        self.root = Node()

    def get_idx(self, symbol: str) -> int:
        return ord(symbol) - ord('a')

    def add_string(self, s: str) -> None:
        cur_node = self.root
        for i in range(len(s) - 1, -1, -1):
            idx = self.get_idx(s[i])
            if cur_node.children[idx] is None:
                cur_node.children[idx] = Node()
            cur_node = cur_node.children[idx]
        cur_node.is_terminal = True

    def split(self, T: str) -> None:
        dp = [True] + [False] * len(T)
        for i in range(1, len(T) + 1):
            j = i - 1
            cur_node = self.root
            while True:
                idx = self.get_idx(T[j])
                cur_node = cur_node.children[idx]
                if cur_node is None:
                    break
                elif cur_node.is_terminal and dp[j]:
                    dp[i] = True
                    break
                j -= 1
                if j < 0:
                    break
        print('YES') if dp[len(T)] else print('NO')


def main() -> int:
    T, n = input(), int(input())
    splitter = TextSplitter()
    [splitter.add_string(input()) for _ in range(n)]
    splitter.split(T)
    return 0


if __name__ == '__main__':
    main()
