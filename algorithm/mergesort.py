# -*- coding: utf-8 -*-
import random


def merge_sorted_list(sorted_a, sorted_b):
    len_a, len_b = len(sorted_a), len(sorted_b)
    a, b = 0, 0
    new_sorted_seq = []
    while a < len_a and b < len_b:
        if sorted_a[a] <= sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    if a < len_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left_part = merge_sort(array[:mid])
        right_part = merge_sort(array[mid:])
        return merge_sorted_list(left_part, right_part)


def test_merge_sort():
    ll = list(range(10))
    random.shuffle(ll)
    new_list = merge_sort(ll)
    print(new_list)
    assert new_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    test_merge_sort()
