# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        h = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l))
        
        dummy = ListNode(0)
        cur = dummy
        while h:
            val, i, l = heapq.heappop(h)
            cur.next = l
            cur = cur.next
            if l.next:
                node =l.next
                l.next = None
                heapq.heappush(h, (node.val, i, node))
        return dummy.next

