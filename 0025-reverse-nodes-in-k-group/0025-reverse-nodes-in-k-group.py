# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 1:
            return head

        # reverse one linked list
        def reverse(node):
            cur = node
            prev = None
            while cur:
                node = cur.next
                cur.next = prev
                prev = cur
                cur = node
            return prev
            
        # find the start node and the next start node
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        node = head
        while node:
            start = node
            for _ in range(k - 1):
                if node.next:
                    node = node.next
                else:
                    return dummy.next
            end = node
            next_start = node.next

            end.next = None
            new_start = reverse(start)
            prev.next = new_start
            start.next = next_start
            node = next_start
            prev = start
        return dummy.next
25