# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        cur = head
        prev = dummy
        dummy2 = ListNode()
        new = dummy2
        while cur:
            if cur.val >= x:
                node = cur.next
                prev.next = node
                cur.next = None
                new.next = cur
                cur = node
                new = new.next
            else:
                prev = cur
                cur = cur.next
                
        
        if dummy2.next:
            prev.next = dummy2.next
        
        return dummy.next
            
