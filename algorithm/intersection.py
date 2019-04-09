# coding: utf-8
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length_a = 0
        cur = headA
        while cur and cur.next:
            length_a += 1
            cur = cur.next

        length_b = 0
        cur = headB
        while cur and cur.next:
            length_b += 1
            cur = cur.next

        if length_a > length_b:
            steps = length_a - length_b
            curA = headA
            while steps > 0:
                steps -= 1
                curA = curA.next
            curB = headB
        else:
            steps = length_b - length_a
            curB = headB
            while steps > 0:
                steps -= 1
                curB = curB.next
            curA = headA

        while curA and curB:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None

