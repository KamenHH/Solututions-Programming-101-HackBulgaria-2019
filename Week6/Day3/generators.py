def chain(iterable_one, iterable_two):
    try:
        iter(iterable_one)
        iter(iterable_two)
    except TypeError:
        print('Error, provided objects are not iterable!')
        exit(-1)
    for iterable in (iterable_one, iterable_two):
        for item in iterable:
            yield item


def compress(iterable, mask):
    for pair in zip(iterable, mask):
        if pair[1]:
            yield pair[0]


def cycle(iterable):
    index = 0
    while True:
        try:
            yield iterable[index]
            index += 1
        except IndexError:
            index = 0

        
def main():
    # print(list(chain(range(1,6), range(6,10))))
    # print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    endless = cycle(range(1,5))
    for i in endless:
        print(i)


if __name__ == '__main__':
    main()
