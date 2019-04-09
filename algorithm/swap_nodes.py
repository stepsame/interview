# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归，回溯思想
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        next = head.next
        head.next = self.swapPairs(head.next.next)
        next.next = head
        return next


# 1->2->3->4