# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        dummy = ListNode(next=head)
        size = 1
        while size < n:
            prev, cur = dummy, dummy.next
            while cur:
                left = cur
                right = self.split(left, size)
                cur = self.split(right, size)
                prev.next = self.merge(left, right)
                while prev.next:
                    prev = prev.next
            size *= 2
        return dummy.next

    def split(self, head, size):
        for _ in range(size - 1):
            if not head:
                break
            head = head.next
        if not head:
            return None
        rest, head.next = head.next, None
        return rest
    
    def merge(self, a, b):
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next
