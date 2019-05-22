# -*- coding: utf-8 -*-
import random


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(array, begin, end):
    if begin >= end:
        return
    split_point = partition(array, begin, end)
    quick_sort_helper(array, begin, split_point - 1)
    quick_sort_helper(array, split_point + 1, end)

def partition(array, begin, end):
    pivot_value = array[begin]
    left, right = begin + 1, end
    while True:
        while left <= right and array[left] <= pivot_value:
            left += 1
        while left <= right and array[right] > pivot_value:
            right -= 1
        if left > right:
            break
        array[left], array[right] = array[right], array[left]
    array[begin], array[right] = array[right], array[begin]

    return right
    


def test():
    ll = [i for i in range(10)]
    random.shuffle(ll)
    print(ll)
    quick_sort(ll)
    print(ll)
    assert ll == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    test()
