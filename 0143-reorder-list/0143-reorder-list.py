# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        
        #split the linked list from the middle
            #find the middle node of the linked list
            
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #spilt the linked list
        #reverse the right part of the split linked list
        prev = None
        cur = slow.next
        slow.next = None    
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        #[12]|[43]   
            
        #merge the two linked list together
        while head and prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2
        
            
        
        
        
        
        
        
        
        