# -*- coding: utf-8 -*-
import random


def binary_search(sorted_array, target):
    if sorted_array is None:
        return -1

    begin = 0
    end = len(sorted_array) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target:
            end = mid - 1
        else:
            begin = mid + 1
    return -1


def test_binary_search():
    ll = list(range(10))
    print(binary_search(ll, 7))
    assert binary_search(ll, 7) == 7


if __name__ == '__main__':
    test_binary_search()
