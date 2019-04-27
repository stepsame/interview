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

# 循环，增加 dummy node

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            first.next = second.next
            cur.next = second
            second.next = first
            cur = cur.next.next
        return dummy.next
        