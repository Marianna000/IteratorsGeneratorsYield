class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.len = len(list_of_list) #3


    def __iter__(self):
        print('start of the cycle')
        self.counter = -1
        self.values = []
        return self

    def __next__(self):
        self.counter += 1

        for val in self.list[self.counter]:
            self.values.append(val)

        if self.counter <= self.len:
            raise StopIteration


        return self.values

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