# coding: utf-8
# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路1：合并两个有序链表的思路，两个指针
# 思路2：比较 k 个头节点
# 思路3：最小堆

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for l in lists:
            while l:
                h.append(l.val)
                l = l.next
        heapq.heapify(h)

        root = ListNode(None)
        cur = root
        while h:
            val = heapq.heappop(h)
            n = ListNode(val)
            cur.next = n
            cur = cur.next
        return root.next

