# -*- coding: utf-8 -*-
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 循环的方式


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


# 递归的方式
# 思路： 假设 k 之后都已经反转，如何处理 k ? k + 1 指向 k, k 指向 none
class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        # 1->2->3->4->5->None
        # 5->4->3->2->1->None
        if not head or not head.next:
            return head
        p = self.reverse_list(head.next)
        next_node = head.next
        next_node.next = head
        head.next = None
        return p


