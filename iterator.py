from itertools import chain


class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.counter = 0
        self.storage = []


    def __iter__(self):
        print('start of the cycle')
        return self


    def __next__(self):

        if self.counter >= len(self.list):
            if self.storage:
                # Дошли до конца вложенного списка,
                # выходим из него во внешний, "вспоминаем" состояние
                self.list, self.counter = self.storage.pop()
                return next(self)
            else:
                raise StopIteration
        item = self.list[self.counter]
        self.counter += 1

        if type(item) is not list:
            return item
        else:
            # Запоминаем текущее состояние
            self.storage.append((self.list, self.counter))
            # Входим во вложенный список, он становится текущим списком
            self.list = item
            self.counter = 0
            return next(self)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(list(FlatIterator(list_of_lists_1)))

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]