
nested_list = [
	['a', 'b', 'c', [1, 2, [3, 4]]],
	['d', 'e', 'f', [5, [6]], 'h', False],
	[1, 2, None],
]


def flat_generator(lst) :
    for i in lst :
        if isinstance(i, list) :
            yield from flat_generator(i)
        else :
            yield i


if __name__ == '__main__' :
    # for i in flat_generator(nested_list) :
    #     print(i)
    gen = flat_generator(nested_list)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
