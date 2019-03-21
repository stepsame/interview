# -*- coding: utf-8 -*-
import random


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0  # 选择第一个元素作为 pivot
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
        great_part = [i for i in array[pivot_index + 1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test():
    ll = [i for i in range(10)]
    random.shuffle(ll)
    new_ll = quick_sort(ll)
    assert new_ll == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    test()
