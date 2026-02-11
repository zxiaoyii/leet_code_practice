# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_g = dummy
        #get the group of kth nodes
            #if there is k nodes exits
        #[dummy ,1, 2, 3, 4, 5] k = 2
        # prev_g   kth
        while True:
            kth = self.getKth(prev_g, k)  
            if not kth:
                break    
            #reverse the group of nodes
            prev, cur = kth.next, prev_g.next
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
            #dummy -> 2 -> 1 -> 3 -> 4 -> 5    
            #prev_g  kth
            #connect the group of nodes to the orignal linked list
            temp1 = prev_g.next
            prev_g.next = kth
            prev_g = temp1
        #return the head of the modified linked list
        return dummy.next
    
    def getKth(self, node, k):
        cur = node
        for _ in range(k):
            if not cur.next:
                return None
            cur = cur.next
        return cur
        