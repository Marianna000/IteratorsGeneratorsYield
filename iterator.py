class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list


    def __iter__(self):
        print('start of the cycle')
        self.values = []
        return self

    def __next__(self):

        for val in self.list:
            for item in val:
                self.values.append(item)
        return self.values

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]