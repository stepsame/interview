# -*- coding: utf-8 -*-
import random


def heap_sort(array):
    from heapq import heappop, heappush
    items = []
    for value in array:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]


def test():
    ll = [i for i in range(10)]
    random.shuffle(ll)
    print(ll)
    new_ll = heap_sort(ll)
    print(new_ll)
    assert new_ll == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    test()
