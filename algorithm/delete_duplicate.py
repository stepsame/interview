# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            next_node = cur.next
            if cur.val == next_node.val:
                cur.next = next_node.next
            else:
                cur = cur.next
        return head
