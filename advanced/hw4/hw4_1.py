

class FlatIterator() :
    def __init__(self, nested_list) :
        self.flat_list = []
        self.crete_flat_list(nested_list)
        self.current_element = -1


    def crete_flat_list(self, lst) :
        new_lst = lst[::-1]
        while len(new_lst) > 0 :
            elem = new_lst.pop()
            if isinstance(elem, list) :
                self.crete_flat_list(elem)
            else :
                self.flat_list.append(elem)


    def __iter__(self) :
        return self

    def __next__(self) :
        self.current_element += 1
        if self.current_element == len(self.flat_list) :
            raise StopIteration
        return self.flat_list[self.current_element]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


nested_list2 = [
	['a', 'b', 'c', [1, 2, 3, 4, [5, 6]]],
	['d', 'e', 'f', [7, 8], 'h', False],
	[1, 2, [9, 10], None],
]


if __name__ == '__main__' :
    # test = FlatIterator(nested_list2)
    # print(test.flat_list)
    # for i in test :
    #     print(i)
    for i in FlatIterator(nested_list2) :
        print(i)



