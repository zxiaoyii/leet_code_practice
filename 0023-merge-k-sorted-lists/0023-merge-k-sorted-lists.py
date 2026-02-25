# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        heap = []
        # traverse all the list in lists and add the first node into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        cur = dummy
        # while heap is not empty
            # pop temp_node and add to the result linked list
            # add the node next to temp_node to the heap
        while heap:
            temp_val, temp_i, temp_node = heapq.heappop(heap) 
            cur.next = temp_node
            cur = cur.next  
            if temp_node.next:
                heapq.heappush(heap, (temp_node.next.val, temp_i, temp_node.next)) 
            
        return dummy.next