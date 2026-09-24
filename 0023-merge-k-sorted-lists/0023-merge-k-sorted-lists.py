# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        dummy = ListNode()
        node = dummy
        while heap:
            val, i, n = heapq.heappop(heap)
            node.next = n
            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))
            node = node.next
        return dummy.next