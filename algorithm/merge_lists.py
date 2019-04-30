# coding: utf-8
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路1：合并两个有序链表的思路，两个指针
# 思路2：比较 k 个头节点
# 思路3：最小堆

import heapq
class Solution:
    def mergeKLists(self, lists) -> ListNode:

        h = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapq.heapify(h)
        head = ListNode(None)
        cur = head
        while h:
            val, index, node = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(h, (node.val, index, node))
        return head.next

if __name__ == '__main__':
    s = Solution()
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    a.next = d
    print(s.mergeKLists([a, b, c]).val)