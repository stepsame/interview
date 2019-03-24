# -*- coding: utf-8 -*-
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 循环的方式
# 递归的方式


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        # 1->2->3->4->5->None
        # 5->4->3->2->1->None
        pre, cur = None, head

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        return pre


